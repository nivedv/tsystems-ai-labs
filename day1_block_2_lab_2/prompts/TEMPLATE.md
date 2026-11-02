# Five parts of a good prompt (use this to write triage_v1)

1. **Role**    : who the model acts as.
2. **Task**    : one clear job.
3. **Context** : what it needs (the allowed categories, the rules).
4. **Format**  : the exact shape of the answer. Our check wants a JSON object with 4 fields:
                 `category`, `priority`, `summary`, `next_step`.
5. **Limits**  : what it must not do.

What the check function accepts (these are the acceptance criteria):
- the reply parses as JSON (so: JSON only, no extra words, no markdown)
- all four fields are present
- `category` is one of: access, network, hardware, software, other
- `priority` is the NUMBER 1, 2 or 3 (not the text "2")
- `summary` has 20 words or fewer

Write your prompt in plain text in `triage_v1.txt` (replace the placeholder line).
For `triage_v2.txt`: copy v1, then change ONE thing. Write what and why in `VERSION_LOG.md`.
