# Lab 4 hints (try 5 minutes first, then open level 1)

## TODO 1: the knowledge base for this run
- **Level 1.** `kb_full` is a dictionary. You want a new dictionary without some keys. Do not delete files.
- **Level 3.**
```python
kb_run = {art_id: text for art_id, text in kb_full.items() if art_id not in args.exclude}
```

## TODO 2: retrieve, ask, check
- **Level 1.** The same five actions as in Lab 3: search, build messages, call the model, check the citations. Plus: is the key article cited?
- **Level 2.** Use `kb_run` (not `kb_full`) in both `search` and `build_messages`. The helper functions `citations.check_citations` and `citations.cited_ids` are ready.
- **Level 3.**
```python
hits = rag_lib.search(q["text"], kb_run, k=args.k)
retrieved = [h[0] for h in hits]
if args.retrieval_only:
    answer, check, right, tokens = "", "-", None, 0
else:
    messages = rag_lib.build_messages(q["text"], hits, kb_run)
    resp, _ = common.call_model(client, deployment, messages)
    answer = resp.choices[0].message.content or ""
    check = citations.check_citations(answer, retrieved)
    right = q["key"] in citations.cited_ids(answer)
    tokens = resp.usage.total_tokens
```

## TODO 3: summary
- **Level 3.**
```python
n = len(rows)
valid = sum(1 for r in rows if r["check"].startswith("pass"))
right_n = sum(1 for r in rows if r["right"])
print(f"\ncitation valid       : {valid} / {n}")
print(f"right article cited  : {right_n} / {n}")
print(f"total tokens         : {sum(r['tokens'] for r in rows)}   per question: {sum(r['tokens'] for r in rows) // n}")
fluent_wrong = [r["id"] for r in rows if r["check"].startswith("pass") and not r["right"] and "not found" not in r["answer"].lower()]
if fluent_wrong:
    print(f"WATCH: valid citation but NOT the right article (fluent and wrong): {', '.join(fluent_wrong)}")
```

## Common problems
| What you see | What to do |
|---|---|
| Score is wrong for every question | Is the answer key loaded? `right` uses `q["key"]`. |
| k=1 gives no change | Print `retrieved` for both runs (`--retrieval-only`). Did the ids change? |
| You changed k in two places | Use only `args.k`. |
| You deleted an article file | Restore it with `git checkout kb/`. Next time use `--exclude`. |
| 429 | Wait 30 seconds; the script has `--pause`. |
