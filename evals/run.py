#!/usr/bin/env python3
"""Capture isolated Codex runs; grading is evidence-based and deliberately separate."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import time
import tomllib


ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ("SKILL.md", "agents", "references", "assets")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def skill_files(skill):
    for name in RESOURCES:
        path = skill / name
        if path.is_file():
            yield path
        elif path.is_dir():
            yield from sorted(p for p in path.rglob("*") if p.is_file())


def run_case(case, args, version, config):
    result = args.output / args.variant / ("activation" if args.activation else case["split"]) / case["id"]
    result.mkdir(parents=True, exist_ok=False)
    workspace = result / "workspace"
    workspace.mkdir()
    subprocess.run(["git", "init", "-q", str(workspace)], check=True)
    inputs = {}
    for name in case.get("files", []):
        source = ROOT / "evals" / "fixtures" / name
        shutil.copy2(source, workspace / name)
        inputs[name] = digest(source)

    manifest = {}
    if args.skill:
        target = workspace / ".agents" / "skills" / "rockefeller"
        target.mkdir(parents=True)
        for source in skill_files(args.skill):
            relative = source.relative_to(args.skill)
            destination = target / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            manifest[str(relative)] = digest(source)

    # Neither expectations nor grading instructions are given to the respondent.
    prompt = case["prompt"]
    if not args.activation:
        prefix = "Use $rockefeller.\n\n" if args.skill else ""
        prompt = prefix + prompt + (
            "\n\nUse only the supplied scenario and workspace files. Do not browse, "
            "use other skills, access live accounts, or take external actions. "
            "Return your analysis in the final answer; do not modify input files."
        )
    (result / "prompt.txt").write_text(prompt + "\n")
    command = [
        "codex", "exec", "--ephemeral", "--sandbox", "read-only",
        "--disable", "apps", "--disable", "plugins", "--disable", "hooks",
        "--disable", "browser_use", "--disable", "computer_use", "--disable", "multi_agent",
        "-c", 'web_search="disabled"',
        "-c", 'approval_policy="never"', "--color", "never", "--json",
        "--cd", str(workspace), "--output-last-message", str(result / "answer.md"), "-",
    ]
    # Disable every locally configured MCP server without exposing its credentials.
    for server in config.get("mcp_servers", {}):
        command[2:2] = ["-c", f"mcp_servers.{server}.enabled=false"]
    started = time.monotonic()
    status = "completed"
    with (result / "trace.jsonl").open("w") as out, (result / "stderr.log").open("w") as err:
        process = subprocess.Popen(
            command, stdin=subprocess.PIPE, stdout=out, stderr=err,
            text=True, start_new_session=True,
        )
        try:
            process.communicate(prompt, timeout=args.timeout)
        except subprocess.TimeoutExpired:
            status = "timeout"
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.communicate(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.communicate()

    answer = result / "answer.md"
    if status == "completed" and (process.returncode or not answer.is_file() or not answer.read_text().strip()):
        status = "infrastructure-error"
    unchanged = all(digest(workspace / name) == value for name, value in inputs.items())
    metadata = {
        "case": case["id"], "variant": args.variant, "activation": args.activation,
        "utc": datetime.now(timezone.utc).isoformat(), "cli_version": version,
        "configured_model": config.get("model"),
        "configured_reasoning_effort": config.get("model_reasoning_effort"),
        "command": command, "skill_sha256": manifest, "input_sha256": inputs,
        "inputs_unchanged": unchanged, "status": status, "exit_code": process.returncode,
        "elapsed_seconds": round(time.monotonic() - started, 2),
    }
    (result / "run.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps({key: metadata[key] for key in ["case", "variant", "status", "inputs_unchanged", "elapsed_seconds"]}), flush=True)
    return status == "completed" and unchanged


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", type=Path, help="Skill directory; omit for the no-skill baseline")
    parser.add_argument("--variant", required=True, choices=["original", "revised", "none"])
    parser.add_argument("--output", type=Path, required=True, help="New results outside this checkout")
    parser.add_argument("--case", action="append", default=[], help="Select a case ID; repeat as needed")
    parser.add_argument("--holdout", action="store_true")
    parser.add_argument("--activation", action="store_true")
    parser.add_argument("--jobs", type=int, default=1, choices=[1, 2])
    parser.add_argument("--timeout", type=int, default=300, help="Seconds per run")
    parser.add_argument("--list", action="store_true", help="List selected IDs without running Codex")
    args = parser.parse_args()
    args.output = args.output.resolve()
    if args.output == ROOT or ROOT in args.output.parents:
        parser.error("Store raw results outside the source checkout.")
    if args.output == Path.home() or args.output == Path("/"):
        parser.error("Choose a dedicated results directory.")
    if (args.variant == "none") != (args.skill is None):
        parser.error("Use --skill for original/revised and omit it for none.")
    if args.activation and (args.holdout or args.skill is None):
        parser.error("Activation requires a skill and cannot be combined with --holdout.")
    if args.timeout <= 0:
        parser.error("--timeout must be positive.")
    if args.skill:
        args.skill = args.skill.resolve()
        if not (args.skill / "SKILL.md").is_file():
            parser.error("--skill must contain SKILL.md.")
        if args.output == args.skill or args.skill in args.output.parents:
            parser.error("Store raw results outside the skill directory.")

    path = ROOT / "evals" / ("activation.jsonl" if args.activation else "cases.jsonl")
    cases = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    ids = [case["id"] for case in cases]
    if len(ids) != len(set(ids)):
        parser.error("Duplicate case IDs.")
    if set(args.case) - set(ids):
        parser.error("Unknown case IDs: " + ", ".join(sorted(set(args.case) - set(ids))))
    for case in cases:
        if not case["id"] or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-" for c in case["id"]):
            parser.error("Case IDs must contain lowercase letters, digits and hyphens.")
        for name in case.get("files", []):
            if Path(name).name != name or not (ROOT / "evals" / "fixtures" / name).is_file():
                parser.error("Invalid fixture: " + name)
    split = "holdout" if args.holdout else "development"
    selected = [case for case in cases if (args.activation or case["split"] == split) and (not args.case or case["id"] in args.case)]
    if not selected:
        parser.error("No cases selected for this split.")
    if set(args.case) - {case["id"] for case in selected}:
        parser.error("A selected case belongs to another split; use --holdout separately.")
    if args.list:
        print("\n".join(case["id"] for case in selected))
        return
    args.output.mkdir(parents=True, exist_ok=True)
    # Fail before any run rather than partially overwriting a prior comparison.
    for case in selected:
        group = "activation" if args.activation else case["split"]
        if (args.output / args.variant / group / case["id"]).exists():
            parser.error("Result already exists; use a fresh --output directory.")
    version = subprocess.check_output(["codex", "--version"], text=True).strip()
    config_path = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "config.toml"
    config = tomllib.loads(config_path.read_text()) if config_path.is_file() else {}
    if any(not re.fullmatch(r"[A-Za-z0-9_-]+", name) for name in config.get("mcp_servers", {})):
        parser.error("Cannot safely override this MCP server name using CLI dotted keys; isolate the host configuration first.")
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        outcomes = list(pool.map(lambda case: run_case(case, args, version, config), selected))
    if not all(outcomes):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
