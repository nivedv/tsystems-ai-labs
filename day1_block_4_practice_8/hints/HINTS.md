# Practice hints

## TODO 1: recall_at_k
- **Level 1.** For each question: take the ids of the top k results. Is `q["key"]` among them? Count the yes answers, divide by the number of questions.
- **Level 3.**
```python
hits = 0
for q in questions:
    top = [h[0] for h in rag_lib.search(q["text"], kb, k=k)]
    if q["key"] in top:
        hits += 1
return hits / len(questions)
```

## TODO 2: groundedness on hits
- **Level 1.** First keep only the rows where `r["key"]` is in `r["retrieved"]`. Then, among them, count those whose answer cites `r["key"]`.
- **Level 3.**
```python
hit_rows = [r for r in rows if r["key"] in r["retrieved"]]
right = [r for r in hit_rows if r["key"] in citations.cited_ids(r["answer"])]
grounded = len(right) / len(hit_rows) if hit_rows else None
```

## Common problems
| What you see | What to do |
|---|---|
| `k3.json not found` | Run step 0. |
| recall goes DOWN when k goes up | There is a bug. Search for k=1 must be inside the result for k=2. |
| groundedness is n/a | No hit rows. Check `r["retrieved"]` and `r["key"]`. |
