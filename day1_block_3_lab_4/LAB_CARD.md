# Lab 4 · Break retrieval and measure the drop
**Time:** 18:35-19:05 (30 min) · **Work:** alone · **Folder:** `day1_block_3_lab_4`

## Your question
Your manager asks: **"If we cut k to save cost, how much quality do we lose?"**
You cannot answer with an opinion. You answer with **numbers from your own pipeline**.

## Two scores for every run (6 questions, new question set B)
- **Citation valid:** the Demo 6 check passes.
- **Right article cited:** the answer cites the one article that really answers the question (the answer key is in `data/lab4_questions.json`).
Use the **same six questions** in every run so the numbers can be compared.

## Steps and time
| Time | What you do |
|---|---|
| 18:35-18:42 | Finish TODO 1, 2, 3. Run the **baseline** (k=2) and **save it**. Save before you break anything. |
| 18:42-18:49 | **Break A:** k=1. Run again. Write both scores, even if the drop is zero. |
| 18:49-18:56 | **Break B:** pick ONE question that your baseline answered with the right article. Remove its article for that run only. Run that one question. What does the helper say? Copy the sentence. |
| 18:56-19:01 | Stretch: k=3 and k=4. Note the tokens each time. |
| 19:01-19:05 | Fill the table, restore (nothing to restore: files are untouched), save, share-out. |

## Commands (from the repo root)
```
python day1_block_3_lab_4/scripts/lab4_break.py --k 2 --label baseline --save
python day1_block_3_lab_4/scripts/lab4_break.py --k 1 --label breakA_k1 --save
python day1_block_3_lab_4/scripts/lab4_break.py --k 2 --exclude KB-010 --questions b1 --label breakB --save
python day1_block_3_lab_4/scripts/lab4_break.py --k 3 --label k3 --save
python day1_block_3_lab_4/scripts/lab4_break.py --k 4 --label k4 --save
python day1_block_3_lab_4/scripts/compare_runs.py
```
(For Break B choose the article of the question you want. Example: question b1 → article KB-010 in the answer key.)
No model calls and no cost: add `--retrieval-only` to see what search returns.

## You are done when
- [ ] Baseline, Break A and Break B are saved in `results/`
- [ ] `results/RESULT_TABLE.md` is filled in
- [ ] You wrote the **one sentence for your manager**, with real numbers

## Remember
- **If you see no drop, congratulations on your honesty.** Then check: did k=1 change the retrieved ids? Use `--retrieval-only` to compare. That is the debug order from Demo 5.
- A **valid citation with the wrong article** is the dangerous case: fluent, cited and wrong. If you see it in Break B, copy the exact sentence into your table. That is the key finding of this lab.
- Six questions is tiny. One question = about 17 points. Treat the drop as a signal.
- Stuck? 5 minutes, then `hints/HINTS.md`, then raise your hand. 429? Wait 30 seconds.
