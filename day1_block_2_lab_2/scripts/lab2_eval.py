"""Lab 2: A versioned prompt returning schema-valid JSON.   (15:00-15:30)

Manager: "Show me that the triage prompt is ready for the ticket system." Bring acceptance criteria and a pass rate.
Test set = 5 tickets x 3 runs = 15 runs per version. The check function is ready in lib/checks.py.

You complete THREE small TODO blocks. Everything else is ready.

  python day1_block_2_lab_2/scripts/lab2_eval.py --prompt prompts/triage_v1.txt --dry-run
  python day1_block_2_lab_2/scripts/lab2_eval.py --prompt prompts/triage_v1.txt
  python day1_block_2_lab_2/scripts/lab2_eval.py --prompt prompts/triage_v2.txt
  python day1_block_2_lab_2/scripts/lab2_eval.py --prompt prompts/triage_v2.txt --include-edge     # stretch task
"""
import argparse
import json
import pathlib
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "lib"))
import checks  # noqa: E402
import common  # noqa: E402

LAB = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = json.loads((LAB / "schemas/triage.schema.json").read_text(encoding="utf-8"))

ap = argparse.ArgumentParser(description="Lab 2: prompt versions and pass rate")
ap.add_argument("--prompt", required=True, help="prompt file, relative to this lab folder, e.g. prompts/triage_v1.txt")
ap.add_argument("--runs", type=int, default=3)
ap.add_argument("--include-edge", action="store_true", help="stretch task: add the 2 edge tickets")
ap.add_argument("--pause", type=float, default=0.5, help="seconds between calls (helps with rate limits)")
ap.add_argument("--dry-run", action="store_true")
args = ap.parse_args()

data = json.loads((LAB / "data/tickets_lab2.json").read_text(encoding="utf-8"))
todo = data["core"] + (data["edge"] if args.include_edge else [])
version = pathlib.Path(args.prompt).stem

# TODO 1: read the prompt file (the path is LAB / args.prompt) into the variable "system".
system = None
if system is None:
    sys.exit("TODO 1 is not done yet: read the prompt file into 'system'. See hints/HINTS.md")
if "WRITE YOUR PROMPT HERE" in system or "COPY v1 HERE" in system:
    sys.exit(f"{args.prompt} still has the placeholder. Write your prompt in that file first.")

print(f"Prompt {version}: {len(system.split())} words. Tickets: {len(todo)}  x runs: {args.runs}  = {len(todo) * args.runs} calls")
if args.dry_run:
    print("\n" + system + "\n\nDry run only. No call was made.")
    raise SystemExit(0)

client, deployment = common.get_client()
counts = {r: 0 for r in checks.REASONS}
log = []
for t in todo:
    for run in range(1, args.runs + 1):
        # TODO 2: build the messages (system + the ticket text t["text"]), call the model, and get the reply text.
        #         Then ask the check function for the reason:  checks.check_triage(reply, SCHEMA)
        #         Set both variables:  reply  and  reason
        #         (If a call fails, catch the error and use reason = "api_error" so the lab keeps going.)
        reply, reason = None, None
        if reason is None:
            sys.exit("TODO 2 is not done yet: set reply and reason. See hints/HINTS.md")

        counts[reason] += 1
        print(f"{t['id']} ({t['kind']}) run {run}: {reason}")
        log.append({"ticket": t["id"], "run": run, "reason": reason, "reply": reply})
        time.sleep(args.pause)

total = len(todo) * args.runs
# TODO 3: print "<version>: pass X / total", then each failure reason with its count (the dictionary "counts"),
#         then the TOP failure. Finally save counts and log to results/eval_<version>.json
print("TODO 3 is not done yet: no summary and nothing saved. See hints/HINTS.md")
print("Next: write your numbers in results/RESULT_TABLE.md and your change in VERSION_LOG.md")
