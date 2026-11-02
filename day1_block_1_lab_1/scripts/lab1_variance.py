"""Lab 1: Temperature and prompt variance.   (13:20-13:50)

Question from your team lead: "Can we trust the helper to give the same advice twice?"
Collect evidence: run one ticket 5 times at temperature 0, 0.7 and 1.2 = 15 replies. Save them all.

You complete THREE small TODO blocks. Everything else is ready.

  python day1_block_1_lab_1/scripts/lab1_variance.py --learner 3 --dry-run     # see what will run (no calls)
  python day1_block_1_lab_1/scripts/lab1_variance.py --learner 3               # the 15 runs
  python day1_block_1_lab_1/scripts/lab1_variance.py --learner 3 --mode wording   # FALLBACK if temperature is not accepted
"""
import argparse
import json
import pathlib
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "lib"))
import common  # noqa: E402

LAB = pathlib.Path(__file__).resolve().parents[1]

ap = argparse.ArgumentParser(description="Lab 1: temperature and prompt variance")
ap.add_argument("--learner", type=int, help="your learner number (the trainer gives it to you)")
ap.add_argument("--ticket", choices=list("ABCDE"), help="or choose a ticket letter yourself")
ap.add_argument("--mode", choices=["temperature", "wording"], default="temperature")
ap.add_argument("--temps", type=float, nargs="+", default=[0, 0.7, 1.2])
ap.add_argument("--runs", type=int, default=5)
ap.add_argument("--system", default="prompts/lab1_system.txt", help="system prompt file, relative to this lab folder")
ap.add_argument("--out", default="lab1_replies.json")
ap.add_argument("--pause", type=float, default=0.5, help="seconds between calls (helps with rate limits)")
ap.add_argument("--dry-run", action="store_true")
args = ap.parse_args()

if args.ticket is None and args.learner is None:
    sys.exit("Please give --learner <your number>  (or --ticket A..E).")
letter = args.ticket or "ABCDE"[args.learner % 5]
tickets = {t["letter"]: t["text"] for t in json.loads((LAB / "data/tickets_lab1.json").read_text(encoding="utf-8"))["tickets"]}
ticket_text = tickets[letter]
system_text = (LAB / args.system).read_text(encoding="utf-8").strip()

if args.mode == "temperature":
    variants = [(f"temperature {t}", {"temperature": t}, system_text) for t in args.temps]
else:
    ws = json.loads((LAB / "data/wordings_lab1.json").read_text(encoding="utf-8"))["wordings"]
    variants = [(w["id"], {}, w["system"]) for w in ws]

print(f"Ticket {letter}: {ticket_text}")
print(f"Mode: {args.mode}   variants: {[v[0] for v in variants]}   runs each: {args.runs}")
if args.dry_run:
    print("\nSystem prompt (first variant):\n" + variants[0][2])
    print(f"\nDry run only. {len(variants) * args.runs} calls would be made.")
    raise SystemExit(0)

client, deployment = common.get_client()
rows = []
for label, extra, sys_text in variants:
    print(f"\n== {label}")
    for run in range(1, args.runs + 1):
        # TODO 1: build the list "messages": one system message (sys_text) and one user message (ticket_text).
        messages = None
        
]
        if messages is None:
            sys.exit("TODO 1 is not done yet: build the messages list. See hints/HINTS.md")

        # TODO 2: call the model with "messages" and **extra (extra holds the temperature, if any).
        #         Put the text of the answer in the variable "reply".
        reply = None
        
        if reply is None:
            sys.exit("TODO 2 is not done yet: call the model and set reply. See hints/HINTS.md")

        print(f"run {run}: {reply[:90]!r}")
        rows.append({"variant": label, "run": run, "reply": reply})
        time.sleep(args.pause)

# TODO 3: save ALL replies (the list "rows") to results/<args.out> as JSON, with the ticket letter and the mode.
#         The path is:  LAB / "results" / args.out
print("TODO 3 is not done yet: nothing was saved. See hints/HINTS.md")
print("Next: python day1_block_1_lab_1/scripts/compare_replies.py   then READ your replies and fill results/RESULT_TABLE.md")

