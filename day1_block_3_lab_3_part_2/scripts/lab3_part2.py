"""Lab 3 part 2: add a citation gate to your pipeline.   (17:45-18:15)

Service desk lead: "Show me that no answer leaves the helper with a fake or missing source."
Your toolkit from part 1 (rag_lib.py) is reused. Finish TODO 1 and TODO 2 here (TODO 3 is the stretch task).

  python day1_block_3_lab_3_part_2/scripts/lab3_part2.py --test-check     # test your check on 4 saved answers (no model call)
  python day1_block_3_lab_3_part_2/scripts/lab3_part2.py --own "your own question"
  python day1_block_3_lab_3_part_2/scripts/lab3_part2.py --own "..." --retry     # stretch task
"""
import argparse
import json
import pathlib
import re
import sys
import time

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "lib"))
sys.path.insert(0, str(REPO / "day1_block_2_lab_3_part_1" / "scripts"))
import common  # noqa: E402
import rag_lib  # noqa: E402

LAB = pathlib.Path(__file__).resolve().parents[1]


def check_citations(answer, retrieved_ids):
    """Return one of: "pass", "pass_not_found", "fail_no_citation", "fail_fake_citation"."""
    # TODO 1: write the citation check from Demo 6.
    #   1. find all ids like [KB-004] in the answer (a regular expression)
    #   2. if the answer says "not found" (lower-case it first) -> "pass_not_found"
    #   3. if there is no citation -> "fail_no_citation"
    #   4. if any cited id is not in retrieved_ids -> "fail_fake_citation"
    #   5. otherwise -> "pass"
    return None


SAVED = [  # four saved answers to test your check. The retrieved set is ["KB-004", "KB-003"].
    ("good", "Reset your password at the self-service portal [KB-004].", "pass"),
    ("fake", "Reset your password at the self-service portal [KB-009].", "fail_fake_citation"),
    ("none", "Reset your password at the self-service portal.", "fail_no_citation"),
    ("not found", "Not found.", "pass_not_found"),
]

ap = argparse.ArgumentParser()
ap.add_argument("--k", type=int, default=2)
ap.add_argument("--own", help="your own question (the 6th question)")
ap.add_argument("--retry", action="store_true", help="stretch: retry once with a stricter reminder when the check fails")
ap.add_argument("--test-check", action="store_true")
ap.add_argument("--pause", type=float, default=0.5)
args = ap.parse_args()

if args.test_check:
    ok_all = True
    for name, text, expected in SAVED:
        got = check_citations(text, ["KB-004", "KB-003"])
        flag = "OK " if got == expected else "WRONG"
        ok_all &= got == expected
        print(f"{flag} {name:<10} -> {got}   (expected {expected})")
    print("\nYour check works on all 4." if ok_all else "\nYour check is wrong on at least one. Fix it before the next step.")
    print("Rule of testing a test: a check that always passes is broken. Make your own failing answer too.")
    raise SystemExit(0)

data = json.loads((common.ROOT / "data/lab3_questions.json").read_text(encoding="utf-8"))
questions = data["questions"] + [data["probe"]]
own = args.own or input("Type one question of your own: ")
questions.append({"id": "own", "text": own})

kb = rag_lib.load_kb()
if not kb:
    sys.exit("Your part 1 toolkit is not finished (load_kb returns nothing). Finish part 1 first, or ask for the catch-up file.")
client, deployment = common.get_client()

counts = {"pass": 0, "fail_fake_citation": 0, "fail_no_citation": 0, "pass_not_found": 0}
retried = fixed = 0
log = []
for q in questions:
    hits = rag_lib.search(q["text"], kb, k=args.k)
    retrieved = [h[0] for h in hits]
    messages = rag_lib.build_messages(q["text"], hits, kb)
    resp, _ = common.call_model(client, deployment, messages)
    answer = resp.choices[0].message.content or ""
    # TODO 2: run YOUR check on this answer: result = check_citations(answer, retrieved)
    result = None
    if result is None:
        sys.exit("TODO 1 or 2 is not done yet: the check returned nothing. See hints/HINTS.md")

    # TODO 3 (STRETCH, optional): if --retry is on and the result starts with "fail", call the model ONE more time
    #         with the same articles plus this reminder: "You must cite an article ID from the list."
    #         Check again. Count how many fails the retry fixed (retried and fixed are ready for you).

    counts[result] += 1
    print(f"{q['id']:<6} retrieved {retrieved}  ->  {result}")
    print(f"       {answer[:120]!r}")
    log.append({"id": q["id"], "question": q["text"], "retrieved": retrieved, "answer": answer, "result": result})
    time.sleep(args.pause)

print("\nRESULT LOG (6 questions)")
for r, c in counts.items():
    print(f"  {r:<20}{c}")
if args.retry:
    print(f"  retry fixed {fixed} of {retried} fails")
out = LAB / "results" / "lab3_part2.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({"counts": counts, "retried": retried, "fixed": fixed, "log": log}, indent=2), encoding="utf-8")
print("Saved to results/lab3_part2.json. Now fill results/RESULT_TABLE.md. Keep your files: Lab 4 needs this pipeline.")
