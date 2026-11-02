"""Lab 4: Break retrieval and measure the drop.   (18:35-19:05)

Your manager: "If we cut k to save cost, how much quality do we lose?" Answer with numbers from your own pipeline.
Two scores per answer:  citation valid  and  right article cited (the answer key is in data/lab4_questions.json).
Finish TODO 1, 2, 3. Save every run with --save and a --label.

  python day1_block_3_lab_4/scripts/lab4_break.py --k 2 --label baseline --save                      # baseline
  python day1_block_3_lab_4/scripts/lab4_break.py --k 1 --label breakA_k1 --save                     # Break A
  python day1_block_3_lab_4/scripts/lab4_break.py --k 2 --exclude KB-010 --questions b1 --label breakB --save   # Break B
  python day1_block_3_lab_4/scripts/lab4_break.py --k 3 --label k3 --save                            # stretch
  python day1_block_3_lab_4/scripts/compare_runs.py                                                   # the table
"""
import argparse
import json
import pathlib
import sys
import time

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "lib"))
sys.path.insert(0, str(REPO / "day1_block_2_lab_3_part_1" / "scripts"))
import citations  # noqa: E402
import common  # noqa: E402
import rag_lib  # noqa: E402

LAB = pathlib.Path(__file__).resolve().parents[1]

ap = argparse.ArgumentParser()
ap.add_argument("--k", type=int, default=2)
ap.add_argument("--exclude", nargs="*", default=[], help="article ids to remove for THIS RUN only (files stay on disk)")
ap.add_argument("--questions", default="", help="e.g. b1  or  b1,b3   (default: all six)")
ap.add_argument("--label", default="run")
ap.add_argument("--save", action="store_true")
ap.add_argument("--retrieval-only", action="store_true", help="no model calls: only show what search returns")
ap.add_argument("--pause", type=float, default=0.5)
args = ap.parse_args()

questions = json.loads((common.ROOT / "data/lab4_questions.json").read_text(encoding="utf-8"))["questions"]
if args.questions:
    want = set(args.questions.split(","))
    questions = [q for q in questions if q["id"] in want]

kb_full = rag_lib.load_kb()
if not kb_full:
    sys.exit("Your part 1 toolkit is not finished (load_kb returns nothing). Finish part 1 first, or ask for the catch-up file.")

# TODO 1: make "kb_run" = a COPY of kb_full without the articles in args.exclude.
#         (Do not delete files. Only leave them out of this run.)
kb_run = None
if kb_run is None:
    sys.exit("TODO 1 is not done yet: build kb_run. See hints/HINTS.md")

print(f"RUN '{args.label}'  k={args.k}  articles in KB={len(kb_run)}  excluded={args.exclude or 'none'}  questions={len(questions)}")
client = deployment = None
if not args.retrieval_only:
    client, deployment = common.get_client()

rows = []
for q in questions:
    # TODO 2: for this question:
    #   a) hits = search the knowledge base kb_run with k=args.k;  retrieved = the list of article ids in hits
    #   b) build the messages (rag_lib.build_messages with kb_run) and call the model; answer = the text
    #   c) check = citations.check_citations(answer, retrieved)       (this check is provided)
    #   d) right = True if the answer key article q["key"] is among citations.cited_ids(answer)
    #   e) tokens = resp.usage.total_tokens
    #   (if args.retrieval_only is on, skip the model call: answer = "", check = "-", right = None, tokens = 0)
    retrieved = answer = check = right = None
    tokens = 0
    if retrieved is None:
        sys.exit("TODO 2 is not done yet: retrieve, ask, check. See hints/HINTS.md")
    key_in = q["key"] in retrieved
    rows.append({"id": q["id"], "question": q["text"], "key": q["key"], "retrieved": retrieved, "key_retrieved": key_in,
                 "answer": answer, "check": check, "right": right, "tokens": tokens})
    print(f"{q['id']}  retrieved {retrieved}  key {q['key']} {'IN' if key_in else 'MISSING'}  check={check}  right={right}")
    if not args.retrieval_only:
        time.sleep(args.pause)

if args.retrieval_only:
    raise SystemExit(0)

out = LAB / "results" / f"{args.label}.json"
if args.save:
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({"label": args.label, "k": args.k, "exclude": args.exclude, "rows": rows}, indent=2), encoding="utf-8")
    print(f"(saved to results/{out.name})")

# TODO 3: print three numbers for this run:
#   citation valid       = how many rows have a check that starts with "pass"
#   right article cited  = how many rows have right == True
#   total tokens (and tokens per question)
#   Bonus: list the questions that have a valid citation but NOT the right article ("fluent and wrong").
print("TODO 3 is not done yet: no summary printed. See hints/HINTS.md")
