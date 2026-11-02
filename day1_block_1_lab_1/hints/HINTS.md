# Lab 1 hints (try 5 minutes first, then open level 1)

## TODO 1: build the messages
- **Level 1.** The model wants a *list* of messages. Each message is a small dictionary with a `role` and `content`.
- **Level 2.** You need two messages. The first has role `"system"` (the prompt text is in `sys_text`). The second has role `"user"` (the ticket is in `ticket_text`).
- **Level 3.**
```python
messages = [
    {"role": "system", "content": sys_text},
    {"role": "user", "content": ticket_text},
]
```

## TODO 2: call the model
- **Level 1.** Look at how Demo 1 called the model. The helper `common.call_model` does the work.
- **Level 2.** `common.call_model(client, deployment, messages, **extra)` returns two things: the response and the time taken. The reply text is inside `resp.choices[0]...`.
- **Level 3.**
```python
try:
    resp, secs = common.call_model(client, deployment, messages, **extra)
except Exception as e:
    common.explain_error(e)
    if extra:
        print("If temperature is not accepted, run check_temperature.py and use  --mode wording")
    sys.exit(1)
reply = resp.choices[0].message.content or ""
```

## TODO 3: save all replies
- **Level 1.** `rows` is a list of dictionaries. JSON can store it. The folder `results/` may not exist yet.
- **Level 2.** `out = LAB / "results" / args.out`, create the folder, then write `json.dumps(...)` to the file.
- **Level 3.**
```python
out = LAB / "results" / args.out
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({"ticket": letter, "mode": args.mode, "rows": rows}, indent=2), encoding="utf-8")
print(f"\nSaved {len(rows)} replies to results/{args.out}")
```
(In the skeleton, replace the `print("TODO 3 ...")` line with this code.)

## Common problems
| What you see | What to do |
|---|---|
| `Missing settings` | Put the `.env` file in the repo root. Run `python setup/check_env.py`. |
| 400 error mentioning `temperature` | Your deployment does not accept it. Use `--mode wording`. |
| 429 | Wait 30 seconds, then add `--pause 1.5`. |
| `TODO n is not done yet` | That is the script telling you which block to finish. |
