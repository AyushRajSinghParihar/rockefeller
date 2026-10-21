"""CLI contracts that must fail before an evaluation can launch or overwrite data."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RunnerContracts(unittest.TestCase):
    def invoke(self, runner, output, *options):
        return subprocess.run(
            [sys.executable, str(runner), "--variant", "none", "--output", str(output), *options],
            capture_output=True, text=True,
        )

    def test_rejects_invalid_cli_requests_before_model_access(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "results"
            requests = [
                (["--output", str(ROOT / "results"), "--list"], "outside the source"),
                (["--suite", "scenarios", "--case", "missing", "--list"], "Unknown case"),
                (["--suite", "scenarios", "--case", "pricing-cost-holdout", "--list"], "No cases selected"),
                (["--timeout", "0", "--list"], "positive"),
                (["--activation", "--list"], "requires a skill"),
                (["--variant", "revised", "--list"], "Use --skill"),
                (["--variant", "revised", "--skill", str(ROOT), "--activation", "--suite", "scenarios", "--list"], "cannot be combined"),
            ]
            for options, message in requests:
                with self.subTest(options=options):
                    result = self.invoke(ROOT / "evals/run.py", output, *options)
                    self.assertEqual(result.returncode, 2)
                    self.assertIn(message.lower(), result.stderr.lower())
            existing = output / "none/development/narrow-answer"
            existing.mkdir(parents=True)
            sentinel = existing / "answer.md"
            sentinel.write_text("prior evidence\n")
            result = self.invoke(ROOT / "evals/run.py", output, "--case", "narrow-answer")
            self.assertEqual(result.returncode, 2)
            self.assertIn("already exists", result.stderr)
            self.assertEqual(sentinel.read_text(), "prior evidence\n")

    def test_holdouts_require_explicit_selection(self):
        with tempfile.TemporaryDirectory() as temporary:
            for holdout in (False, True):
                options = ["--suite", "scenarios", "--list"] + (["--holdout"] if holdout else [])
                result = self.invoke(ROOT / "evals/run.py", Path(temporary) / "results", *options)
                self.assertEqual(result.returncode, 0, result.stderr)
                selected = set(result.stdout.splitlines())
                self.assertEqual("pricing-cost-holdout" in selected, holdout)
                self.assertEqual("two-resources-holdout" in selected, holdout)
                self.assertEqual("discovery-dialogue" in selected, not holdout)

    def test_rejects_unsafe_outputs_and_malformed_conversations(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "source"
            (project / "evals").mkdir(parents=True)
            runner = project / "evals/run.py"
            shutil.copy2(ROOT / "evals/run.py", runner)
            variants = [
                {"writable_outputs": ["../outside.md"]},
                {"writable_outputs": [".agents/skills/rockefeller/SKILL.md"]},
                {"turns": []},
                {"turns": [{"prompt": "continue", "new_session": "yes"}]},
                {"turns": [{"prompt": "continue"}], "prompt": "both forms"},
            ]
            for variant in variants:
                with self.subTest(variant=variant):
                    case = {"id": "malformed", "split": "development", "files": [], **variant}
                    if "turns" not in variant:
                        case["prompt"] = "test"
                    (project / "evals/scenarios.jsonl").write_text(json.dumps(case) + "\n")
                    result = self.invoke(runner, Path(temporary) / "results", "--suite", "scenarios", "--list")
                    self.assertEqual(result.returncode, 2)
                    self.assertRegex(result.stderr, "Invalid (output path|conversation)")


if __name__ == "__main__":
    unittest.main()
