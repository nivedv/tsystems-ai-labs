"""Lab 3 part 1: RAG with citations.   (16:10-16:40)

Service desk lead: "I will only trust the helper if every answer shows its source."
Finish TODO 1, 2, 3 in rag_lib.py and TODO 4 here. Then run:

  python day1_block_2_lab_3_part_1/scripts/lab3_part1.py --dry-run          # no model call: IDs, scores, prompt
  python day1_block_2_lab_3_part_1/scripts/lab3_part1.py                    # 3 questions with answers
  python day1_block_2_lab_3_part_1/scripts/lab3_part1.py --probe            # stretch: the VPN-7 question
  python day1_block_2_lab_3_part_1/scripts/lab3_part1.py --probe --min-score 2
"""
import argparse
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "lib"))
import common  # noqa: E402
import rag_lib  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--k", type=int, default=2)
ap.add_argument("--min-score", type=int, default=0)
ap.add_argument("--questions", default="L3-1,L3-2,L3-3", help="ids from data/lab3_questions.json")
ap.add_argument("--question", help="or type your own question")
ap.add_argument("--probe", action="store_true", help="stretch: ask the VPN-7 question (no article exists)")
ap.add_argument("--dry-run", action="store_true")
args = ap.parse_args()

data = json.loads((common.ROOT / "data/lab3_questions.json").read_text(encoding="utf-8"))
by_id = {q["id"]: q for q in data["questions"]}
if args.question:
    todo = [{"id": "own", "text": args.question}]
elif args.probe:
    todo = [data["probe"]]
else:
    todo = [by_id[i] for i in args.questions.split(",")]

kb = rag_lib.load_kb()
print(f"Loaded {len(kb)} articles: {', '.join(kb)}")
if not kb:
    sys.exit("TODO 1 is not done yet: load_kb returns nothing. See hints/HINTS.md")

client = deployment = None
if not args.dry_run:
    client, deployment = common.get_client()

for q in todo:
    print("\n" + "=" * 70 + f"\n{q['id']}: {q['text']}")
    ranking = rag_lib.search(q["text"], kb, k=len(kb), min_score=0)
    if ranking is None:
        sys.exit("TODO 2 is not done yet: search returns None. See hints/HINTS.md")
    print("Scores (best first): " + ", ".join(f"{a}={s}" for a, s in ranking[:5]) + " ...")
    hits = rag_lib.search(q["text"], kb, k=args.k, min_score=args.min_score)
    print(f"Top {args.k} kept: {[h[0] for h in hits] or '(nothing passed the minimum score)'}")
    if not hits:
        print("ANSWER: not found   (no model call: no article passed the minimum score)")
        continue
    messages = rag_lib.build_messages(q["text"], hits, kb)
    if messages is None:
        sys.exit("TODO 3 is not done yet: build_messages returns None. See hints/HINTS.md")
    print("\nThe assembled prompt (read it. Is the rule at the top?):")
    for m in messages:
        print(f"  [{m['role']}]")
        for line in m["content"].splitlines():
            print("    " + line)
    if args.dry_run:
        continue

    # TODO 4: call the model with messages (common.call_model returns the response and the time taken).
    #         Put the text of the answer in the variable "answer".
    answer = None
    if answer is None:
        sys.exit("TODO 4 is not done yet: call the model and set answer. See hints/HINTS.md")
    print(f"\nANSWER: {answer}")
    cited = re.findall(r"\[(KB-\d+)\]", answer)
    print(f"IDs cited: {cited or '(none)'}   IDs retrieved: {[h[0] for h in hits]}")
    print("Check ONE sentence of the answer against the article. Did the model add anything?")
