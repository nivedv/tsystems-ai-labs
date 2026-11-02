"""Practice after Demo 8: recall@k and groundedness on YOUR OWN Lab 4 results.   (20:00-20:10)

Step 0 (6 model calls):  python day1_block_3_lab_4/scripts/lab4_break.py --k 3 --label k3 --save
Then finish TODO 1 and TODO 2 and run:
  python day1_block_4_practice_8/scripts/metrics_practice.py
"""
import argparse
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "lib"))
sys.path.insert(0, str(REPO / "day1_block_2_lab_3_part_1" / "scripts"))
import citations  # noqa: E402
import common  # noqa: E402
import rag_lib  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--answers", default="day1_block_3_lab_4/results/k3.json", help="your saved k=3 run, relative to the repo root")
ap.add_argument("--threshold", type=float, default=0.8, help="'high' means at or above this (a rule of thumb)")
args = ap.parse_args()

questions = json.loads((common.ROOT / "data/lab4_questions.json").read_text(encoding="utf-8"))["questions"]
kb = rag_lib.load_kb()
if not kb:
    sys.exit("Your part 1 toolkit is not finished (load_kb returns nothing).")


def recall_at_k(k):
    """Share of the questions whose right article (q["key"]) is among the top k search results."""
    # TODO 1: for every question, take the top k article ids from rag_lib.search(...).
    #         Count the questions where q["key"] is among them. Return count / number of questions.
    return None


print("RETRIEVAL (no model involved)")
recalls = {}
for k in (1, 2, 3):
    r = recall_at_k(k)
    if r is None:
        sys.exit("TODO 1 is not done yet: recall_at_k returns None. See hints/HINTS.md")
    recalls[k] = r
    print(f"  recall@{k} = {r:.2f}")

path = common.ROOT / args.answers
if not path.exists():
    sys.exit(f"{args.answers} not found. Run step 0 first (lab4_break.py with --k 3 --label k3 --save).")
rows = json.loads(path.read_text(encoding="utf-8"))["rows"]

# TODO 2: hit_rows = the rows where the right article (r["key"]) is in r["retrieved"]
#         right    = among hit_rows, the rows whose answer cites r["key"]   (citations.cited_ids(r["answer"]))
#         grounded = len(right) / len(hit_rows)     (None if there are no hit rows)
grounded = "TODO"
hit_rows, right = [], []
if grounded == "TODO":
    sys.exit("TODO 2 is not done yet: compute hit_rows, right, grounded. See hints/HINTS.md")

print(f"\nANSWERS (your k=3 run)")
print(f"  questions where retrieval hit: {len(hit_rows)} of {len(rows)}")
print(f"  groundedness (on hits)       : {'n/a' if grounded is None else f'{grounded:.2f}'}")
for r in hit_rows:
    if r not in right:
        print(f"    - {r['id']}: right article {r['key']} was retrieved but the answer did not cite it")

rec = recalls[3]
hi_r = rec >= args.threshold
hi_g = grounded is not None and grounded >= args.threshold
print("\n2x2 DIAGNOSIS")
print(f"  recall@3 = {rec:.2f} -> {'HIGH' if hi_r else 'LOW'}    groundedness = {'n/a' if grounded is None else f'{grounded:.2f}'} -> {'HIGH' if hi_g else 'LOW'}   (threshold {args.threshold})")
if hi_r and hi_g:
    print("  Box: healthy. Keep watching with the same questions.")
elif hi_r:
    print("  Box: recall high, groundedness low -> fix the PROMPT (rules, citation instruction, examples).")
elif hi_g:
    print("  Box: recall low, groundedness high -> fix SEARCH (k, scoring, article text).")
else:
    print("  Box: both low -> fix SEARCH first, then measure the prompt again.")
print("Write your numbers and your box in results/RESULT_TABLE.md. Six questions: one question = about 17 points.")
