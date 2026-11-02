# Lab 3 part 1 hints (try 5 minutes first, then open level 1)

## TODO 1: load_kb
- **Level 1.** Each file looks like: `ID: KB-004`, `Title: ...`, `Text: ...`. You want one string per article.
- **Level 2.** Split the raw text on `"Title:"` and on `"Text:"`. Join title and text with a full stop.
- **Level 3.**
```python
title = raw.split("Title:", 1)[1].split("Text:", 1)[0].strip()
body = raw.split("Text:", 1)[1].strip()
kb[path.stem] = f"{title}. {body}"
```

## TODO 2: search
- **Level 1.** For each article: how many of the question's words appear in it? That count is the score.
- **Level 2.** `textutils.words(text)` gives a list of words. Turn both lists into sets; the overlap is `q_words & article_words`. Sort with `key=lambda r: (-r[1], r[0])`.
- **Level 3.**
```python
q = set(textutils.words(question))
scored = []
for art_id, text in kb.items():
    score = len(q & set(textutils.words(text)))
    scored.append((art_id, score))
scored.sort(key=lambda r: (-r[1], r[0]))
return [r for r in scored if r[1] >= min_score][:k]
```

## TODO 3: build_messages
- **Level 1.** Look at the prompt you saw in Demo 5. Two messages: system and user.
- **Level 2.** `hits` is a list of `(article_id, score)`. The article text is `kb[article_id]`. Put `[KB-004]` in front of each article.
- **Level 3.**
```python
context = "\n".join(f"[{art_id}] {kb[art_id]}" for art_id, _ in hits)
return [
    {"role": "system", "content": GROUND_RULE},
    {"role": "user", "content": f"{context}\n\nQuestion: {question}"},
]
```

## TODO 4: call the model
- **Level 1.** Same as Lab 1: `common.call_model` returns two things.
- **Level 3.**
```python
resp, _ = common.call_model(client, deployment, messages)
answer = resp.choices[0].message.content or ""
```

## Common problems
| What you see | What to do |
|---|---|
| `TODO n is not done yet` | The script tells you which block to finish. |
| Scores are all 0 | Are you comparing words of the question with words of the article (both through `textutils.words`)? |
| The answer has no citation | Read the assembled prompt. Is the rule at the top? Is each article labelled `[KB-xxx]`? |
| Wrong article first | That is a finding, not a bug in the model. Print the scores. |
