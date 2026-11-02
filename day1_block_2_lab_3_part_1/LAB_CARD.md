# Lab 3 part 1 · RAG with citations
**Time:** 16:10-16:40 (30 min) · **Work:** alone · **Folder:** `day1_block_2_lab_3_part_1` · Part 2 continues at 17:20

## Your question
The service desk lead says: **"I will only trust the helper if every answer shows its source."**
Build the first working version: search → prompt → answer with a citation.

## What you build (your own toolkit, `scripts/rag_lib.py`)
| TODO | Function | What it does |
|---|---|---|
| 1 | `load_kb` | Reads the 10 articles in `kb/` into a dictionary: id → text |
| 2 | `search` | Scores each article against the question (how many different question words it contains) and keeps the top k |
| 3 | `build_messages` | Builds the prompt: rule at the top, the articles with their ids, then the question |
| 4 | in `lab3_part1.py` | Calls the model and gets the answer |

## Steps and time
| Time | What you do |
|---|---|
| 16:10-16:15 | Read this card. Finish **TODO 1**. Run `lab3_part1.py --dry-run`. You should see 10 article IDs. |
| 16:15-16:22 | Finish **TODO 2**. Run again. **Print the scores.** Which article is first? |
| 16:22-16:28 | Finish **TODO 3**. Read the assembled prompt. **Is the rule at the top?** |
| 16:28-16:34 | Finish **TODO 4**. Run without `--dry-run`: 3 questions. Check each citation. |
| 16:34-16:37 | Stretch task. |
| 16:37-16:40 | Save everything. Share-out. |

## Commands (from the repo root)
```
python day1_block_2_lab_3_part_1/scripts/lab3_part1.py --dry-run
python day1_block_2_lab_3_part_1/scripts/lab3_part1.py
python day1_block_2_lab_3_part_1/scripts/lab3_part1.py --probe                # stretch: the VPN-7 question
python day1_block_2_lab_3_part_1/scripts/lab3_part1.py --probe --min-score 2  # stretch: with a minimum score
```

## You are done when
- [ ] Search prints scores and keeps the top 2 articles
- [ ] You can read the assembled prompt and see the rule, the articles and the question
- [ ] You have a cited answer for 3 questions, and the question log in `results/RESULT_TABLE.md` is filled in
(It is OK if you are still at step 3 at 16:37. Cited answers are for the quick ones. Part 2 gives time to catch up.)

## Stretch task
Add a **minimum score**: if no article passes, the helper says "not found" and does **not** call the model. Test it on **VPN-7** (no article exists). Which threshold works? There is no perfect value. That is an engineering decision. Also try a threshold that is too high: what happens to the normal questions?

## Remember
- **Debug order:** (1) look at the retrieval scores, (2) read the assembled prompt, (3) only then the model's answer. A wrong citation: ask "which article did search return?" not "why did the model do this?".
- This log is your **baseline** for Lab 4. Keep your files. Part 2 and Lab 4 reuse `rag_lib.py`.
- Stuck? Try **5 minutes**, then `hints/HINTS.md`, then raise your hand or type "help". 429 error? Wait 30 seconds, then run again.
