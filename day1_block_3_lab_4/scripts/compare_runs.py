"""Helper for Lab 4 (ready to use). Builds your result table from the runs you saved in results/.
Labels it looks for: baseline, breakA_k1, breakB, k3, k4"""
import json
import pathlib

LAB = pathlib.Path(__file__).resolve().parents[1]
RUNS = [("Baseline (k=2)", "baseline"), ("Break A: k=1", "breakA_k1"), ("Break B: article removed", "breakB"),
        ("Stretch: k=3", "k3"), ("Stretch: k=4", "k4")]
base = None
print(f"{'Setting':<26}{'Citation valid':<17}{'Right article':<15}{'Tokens':<9}{'Tokens/question'}")
for title, label in RUNS:
    p = LAB / "results" / f"{label}.json"
    if not p.exists():
        print(f"{title:<26}(not run yet)")
        continue
    d = json.loads(p.read_text(encoding="utf-8"))
    rows = d["rows"]
    n = len(rows)
    valid = sum(1 for r in rows if r["check"].startswith("pass"))
    right = sum(1 for r in rows if r["right"])
    tok = sum(r["tokens"] for r in rows)
    print(f"{title:<26}{f'{valid} / {n}':<17}{f'{right} / {n}':<15}{tok:<9}{tok // n}")
    if label == "baseline":
        base = (right, n, tok // n)
if base:
    print(f"\nBaseline right-article score: {base[0]} / {base[1]}. Write your manager sentence with YOUR numbers:")
    print('"Going from k=2 to k=1 changed the right-article score from __ to __ on 6 questions, and saved __ tokens per question."')
print("Caution: 6 questions is a tiny set. One question = about 17 points.")
