# T-Systems · AI Engineers and AI Quality Specialists · Practice Labs

This repository has the hands-on labs for the course. You work **alone, on your own computer**.
Everything in it is **synthetic** (made up for training). No real company data.

## 1. Set up (5 minutes, do it once)
```
git clone <repo-url>
cd tsystems-ai-labs
python -m venv .venv
# Windows:  .venv\Scripts\activate        Mac/Linux:  source .venv/bin/activate
pip install -r requirements.txt
```
Your trainer will give you a file called **`.env`**. Copy it into this folder (the repo root, next to `README.md`).
Then check everything:
```
python setup/check_env.py
```
You want to see `READY.` at the end. If not, raise your hand or type "help".

## 2. How a lab works
Each lab has its own folder, named by day, block and lab number (for example `day1_block_1_lab_1`).

| File | What it is |
|---|---|
| `LAB_CARD.md` | **Start here.** Your question, steps, time boxes, and when you are done. |
| `scripts/` | The code. Most of it is ready. You finish a few **TODO** blocks. |
| `data/`, `prompts/` | The tickets and prompts for the lab. |
| `results/RESULT_TABLE.md` | Your evidence. Write what you **saw**, not what you expected. |
| `hints/HINTS.md` | Three levels of help. **Try 5 minutes first.** Open level 1, then 2, then 3 only if needed. |

The trainer shows a **demo** first with different tickets and questions. In the lab you do the same method on **new inputs**.

## 3. Rules
- Work alone. Ask for help after 5 minutes of trying. Raise your hand or type "help" in the chat.
- **Never** put the API key in code, in a screenshot, or in git. The `.env` file is ignored by git on purpose.
- A `429` error means "too many requests". Wait 30 seconds and add `--pause 1.5` to the command.
- Save your work at the end of each lab: `git add -A` then `git commit -m "lab 1 done"`. You do **not** need to push.

## 4. Your learner number
The trainer gives you a number from 1 to 14. Lab 1 uses it to choose your ticket.
