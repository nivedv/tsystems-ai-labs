"""Helper for Lab 1 (ready to use). Shows your saved replies side by side and two simple numbers per variant.
The numbers are only an AID. You must READ the replies and decide: same advice? wording differs?

  python day1_block_1_lab_1/scripts/compare_replies.py
  python day1_block_1_lab_1/scripts/compare_replies.py --file lab1_stretch.json
"""
import argparse
import json
import pathlib
import re

LAB = pathlib.Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument("--file", default="lab1_replies.json")
ap.add_argument("--full", action="store_true", help="print full replies")
args = ap.parse_args()

p = LAB / "results" / args.file
if not p.exists():
    raise SystemExit(f"{p.name} not found. Run lab1_variance.py first (and finish TODO 3).")
d = json.loads(p.read_text(encoding="utf-8"))
print(f"Ticket {d['ticket']}  mode: {d['mode']}\n")

variants = []
for r in d["rows"]:
    if r["variant"] not in variants:
        variants.append(r["variant"])


def words(s):
    return set(re.findall(r"[a-z0-9']+", s.lower()))


for v in variants:
    reps = [r["reply"] for r in d["rows"] if r["variant"] == v]
    uniq = len({re.sub(r"\s+", " ", x.strip().lower()) for x in reps})
    sims = []
    for i in range(len(reps)):
        for j in range(i + 1, len(reps)):
            a, b = words(reps[i]), words(reps[j])
            sims.append(len(a & b) / len(a | b) if a | b else 1.0)
    avg = sum(sims) / len(sims) if sims else 1.0
    print(f"=== {v}: {len(reps)} replies, {uniq} different (exact text), average word overlap {avg:.2f} (1.00 = identical)")
    for i, x in enumerate(reps, 1):
        show = x.replace("\n", " ")
        print(f"  {i}. {show if args.full else show[:140]}")
    print()
print("Now READ the replies. For each variant: same advice in 5 of 5?  Wording differs: none / some / a lot?")
