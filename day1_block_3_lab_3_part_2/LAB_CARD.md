# Lab 3 part 2 · Add a citation gate
**Time:** 17:45-18:15 (30 min) · **Work:** alone · **Folder:** `day1_block_3_lab_3_part_2`

## Your question
The service desk lead asks: **"Show me that no answer leaves the helper with a fake or missing source."**
You add a **gate**: a check that every answer must pass.

## Before you start
Part 1 must work (search, prompt, one cited answer). If it does not, finish it in the first 7 minutes. If you are still stuck, ask your trainer for the catch-up file. Do not wait.

## Steps and time
| Time | What you do |
|---|---|
| 17:45-17:52 | Finish part 1: search, prompt, one cited answer. |
| 17:52-18:00 | **TODO 1:** write `check_citations`. Test it: `lab3_part2.py --test-check` (4 saved answers, no model call). Also make **one answer of your own** that should fail. |
| 18:00-18:08 | **TODO 2:** run the 6 questions (4 lab-card questions + VPN-7 + your own). Fill the log. |
| 18:08-18:13 | Stretch task (TODO 3), or catch up. Both are fine. |
| 18:13-18:15 | Save everything. Share-out. |

## Commands (from the repo root)
```
python day1_block_3_lab_3_part_2/scripts/lab3_part2.py --test-check
python day1_block_3_lab_3_part_2/scripts/lab3_part2.py --own "your own question here"
python day1_block_3_lab_3_part_2/scripts/lab3_part2.py --own "your question" --retry     # stretch
```

## What the check must do
1. Find all ids like `[KB-004]` in the answer.
2. If the answer says "not found" (any capital letters, with a full stop) → `pass_not_found`
3. If there is no citation → `fail_no_citation`
4. If any cited id is **not** in the retrieved set → `fail_fake_citation`
5. Otherwise → `pass`

## You are done when
- [ ] Your check is right on the 4 saved answers, and it **fails** on your own bad answer
- [ ] 6 questions are run and the count of pass / fake / none / not found is in `results/RESULT_TABLE.md`
- [ ] Your baseline is saved (Lab 4 breaks this exact pipeline)

## Stretch task
When the check fails, call the model **once more** with the same articles plus the reminder *"You must cite an article ID from the list."* Count how many fails the retry fixes. Is this safety net worth the extra cost?

## Remember
- **A check that always passes is a broken check.** First rule of testing a test.
- Retrieved ids must be **strings** like `"KB-004"`, not tuples. If your check never fails, print `retrieved`.
- The check is a **floor**, not a ceiling. It cannot see a real citation next to a made-up detail.
- Stuck? 5 minutes, then `hints/HINTS.md`, then raise your hand.
