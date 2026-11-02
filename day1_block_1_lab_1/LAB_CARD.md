# Lab 1 · Temperature and prompt variance
**Time:** 13:20-13:50 (30 min) · **Work:** alone, on your own computer · **Folder:** `day1_block_1_lab_1`

## Your question
Your team lead asks: **"Can we trust the helper to give the same advice twice?"**
You must collect **evidence**, not opinions.

## Your ticket
Use your **learner number** (the trainer gives it to you). Your ticket letter is `ABCDE[number mod 5]`:
`1→B  2→C  3→D  4→E  5→A  6→B  7→C  8→D  9→E  10→A  11→B  12→C  13→D  14→E`
(The script does this for you. You can check it with `--dry-run`.)

## Steps and time
| Time | What you do |
|---|---|
| 13:20-13:23 | Open this card. Run `check_temperature.py` (1 call). It tells you which mode to use. Run the script with `--dry-run`. |
| 13:23-13:33 | Finish **TODO 1, 2, 3** in `scripts/lab1_variance.py`. Run it: 3 settings x 5 runs = **15 replies**. |
| 13:33-13:40 | Run `compare_replies.py`. **Read** the replies. Fill `results/RESULT_TABLE.md`. |
| 13:40-13:47 | Stretch task (below). |
| 13:47-13:50 | Share-out. Save your files. |

## Commands (run from the repo root)
```
python day1_block_1_lab_1/scripts/check_temperature.py
python day1_block_1_lab_1/scripts/lab1_variance.py --learner <your number> --dry-run
python day1_block_1_lab_1/scripts/lab1_variance.py --learner <your number>
python day1_block_1_lab_1/scripts/compare_replies.py
```
**If temperature is NOT accepted** (check_temperature says so): add `--mode wording` to the second command.
That runs the same ticket with 3 different prompt wordings, 5 runs each. The lab is the same.

## You are done when
- [ ] 15 replies saved in `results/lab1_replies.json`
- [ ] `results/RESULT_TABLE.md` is filled in, with **what you saw** (not what you expected)

## Stretch task
Rewrite the system prompt so the replies vary **less** at temperature 1.2. Put the new prompt in `prompts/lab1_system_v2.txt`, then run:
```
python day1_block_1_lab_1/scripts/lab1_variance.py --learner <n> --system prompts/lab1_system_v2.txt --temps 1.2 --out lab1_stretch.json
python day1_block_1_lab_1/scripts/compare_replies.py --file lab1_stretch.json
```
Did it help? Write one line in the table. Another good extension: a second ticket (`--ticket C`) at the same three settings.

## Remember
- **One run is not a test.** If you expected the same answer and did not get it, that is the finding.
- Some deployments ignore temperature silently. If all three settings look equally varied, write that in your note.
- Stuck? Try for **5 minutes**, then open `hints/HINTS.md` (level 1 first), then raise your hand or type "help".
- Rate-limit error (429)? Wait 30 seconds, add `--pause 1.5`, run again.
