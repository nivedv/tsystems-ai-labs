# Lab 2 hints (try 5 minutes first, then open level 1)

## Writing the prompt (triage_v1.txt)
- **Level 1.** Use the five parts in `prompts/TEMPLATE.md`. Ask only for JSON, and name the four fields.
- **Level 2.** Say exactly which categories are allowed, say that priority is a *number* 1, 2 or 3, and set a length limit for the summary.
- **Level 3.** Your v1 should contain, in your own words: a role line · "Return only a JSON object. No text before or after. No markdown." · the four field names · the allowed category list · "priority must be 1, 2 or 3 (a number)" · "summary must be 20 words or fewer".

## Choosing the ONE change for v2
Read the failure reasons of v1 first.
| Top failure in v1 | A good single change |
|---|---|
| `not_json` | Stronger format rule, or add one example of a correct reply |
| `schema_fail` | List the allowed values again, say priority is a number |
| `summary_long` | State the word limit as a number and show it in the example |
| nothing fails | Add the rule for unclear tickets ("If unclear: category other, priority 3"). Then run both versions again. |

## TODO 1: read the prompt file
- **Level 1.** The path is `LAB / args.prompt`. Read the text of the file, and remove blank space at both ends.
- **Level 3.**
```python
system = (LAB / args.prompt).read_text(encoding="utf-8").strip()
```

## TODO 2: call the model and check
- **Level 1.** Two things per run: the reply (from the model) and the reason (from `checks.check_triage`).
- **Level 2.** Same pattern as Lab 1: a list of two messages, then `common.call_model(...)`. Wrap the call in `try/except` so one failed call does not stop the lab.
- **Level 3.**
```python
messages = [
    {"role": "system", "content": system},
    {"role": "user", "content": t["text"]},
]
try:
    resp, _ = common.call_model(client, deployment, messages)
    reply = resp.choices[0].message.content or ""
    reason = checks.check_triage(reply, SCHEMA)
except Exception as e:  # keep going if one call fails (for example the empty ticket)
    reply, reason = "", "api_error"
    print(f"   (call failed: {type(e).__name__})")
```

## TODO 3: summary and save
- **Level 1.** `counts` is a dictionary: reason → number. `total` is the number of runs.
- **Level 3.**
```python
print(f"\n{version}: pass {counts['pass']} / {total}")
for r in checks.REASONS[1:]:
    if counts[r]:
        print(f"  {r:<14}{counts[r]}")
failures = {r: c for r, c in counts.items() if r != "pass" and c}
print("Top failure:", max(failures, key=failures.get) if failures else "none")
out = LAB / "results" / f"eval_{version}{'_edge' if args.include_edge else ''}.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({"version": version, "counts": counts, "total": total, "log": log}, indent=2), encoding="utf-8")
print(f"Saved to results/{out.name}")
```
(In the skeleton, replace the `print("TODO 3 ...")` line with this code.)

## Common problems
| What you see | What to do |
|---|---|
| `still has the placeholder` | Replace the first line in the prompt file with your real prompt. |
| Everything is `not_json` | Does your prompt say "only a JSON object, no markdown"? The model often adds three backticks. |
| `schema_fail` | Is priority the text "2" instead of the number 2? Is the category outside the list? |
| 429 | Wait 30 seconds; add `--pause 1.5`. |
