# Practice · recall@k and groundedness on your own results
**Time:** 20:00-20:10 (10 min) · **Work:** alone · **Folder:** `day1_block_4_practice_8`

## Your question
You saw Demo 8. Now compute the same numbers on **your** Lab 4 questions: is the next problem in **search** or in the **prompt**?

## Steps
1. **Step 0 (prepare):** you need a saved run with k=3. If you do not have one: 
   `python day1_block_3_lab_4/scripts/lab4_break.py --k 3 --label k3 --save`
2. Finish **TODO 1** (`recall_at_k`) and **TODO 2** (groundedness on the hit questions) in `scripts/metrics_practice.py`.
3. Run: `python day1_block_4_practice_8/scripts/metrics_practice.py`
4. Write the numbers and **your box** in `results/RESULT_TABLE.md`, with the first fix you would try.

## The two metrics
- **recall@k** = questions whose right article is in the top k ÷ all questions. (No model involved.)
- **groundedness (our proxy)** = among the questions where search found the right article, answers that cite it ÷ those questions.

## Remember
- Do **not** change the prompt or the search now. We only measure.
- IDs in the answer key and in the articles must match exactly (`KB-004`, not `KB4`).
- Six questions: one question = about 17 points. A signal, not proof.
