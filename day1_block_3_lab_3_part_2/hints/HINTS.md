# Lab 3 part 2 hints (try 5 minutes first, then open level 1)

## TODO 1: check_citations
- **Level 1.** Follow the five rules on the lab card in that order. The order matters: "not found" comes first.
- **Level 2.** `re.findall(r"\[(KB-\d+)\]", answer)` returns the ids inside square brackets. Use `answer.lower()` before you look for "not found".
- **Level 3.**
```python
cited = re.findall(r"\[(KB-\d+)\]", answer)
if "not found" in answer.lower():
    return "pass_not_found"
if not cited:
    return "fail_no_citation"
if any(c not in retrieved_ids for c in cited):
    return "fail_fake_citation"
return "pass"
```

## TODO 2: run the check
- **Level 3.**
```python
result = check_citations(answer, retrieved)
```

## TODO 3 (stretch): retry once
- **Level 1.** Only when `--retry` is on and the result starts with `"fail"`. Build the same prompt again, with one extra sentence at the end of the user message.
- **Level 3.**
```python
if args.retry and result.startswith("fail"):
    retried += 1
    reminder = messages[1]["content"] + "\n\nYou must cite an article ID from the list, like [KB-004]."
    resp2, _ = common.call_model(client, deployment, [messages[0], {"role": "user", "content": reminder}])
    answer2 = resp2.choices[0].message.content or ""
    result2 = check_citations(answer2, retrieved)
    print(f"   retry: {result} -> {result2}")
    if result2.startswith("pass"):
        fixed += 1
    answer, result = answer2, result2
```

## Common problems
| What you see | What to do |
|---|---|
| The check passes everything | Test with `--test-check`. A fake id must fail. Print `retrieved` and `cited`. |
| "Not found." is marked as fail | Lower-case the answer first. |
| A retrieved id never matches | Is `retrieved` a list of strings, not tuples? |
| Part 1 is not working | Ask for the catch-up file. Do not wait. |
