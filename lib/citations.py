"""Citation check, PROVIDED for Lab 4 and the practice (so they do not depend on your Lab 3 part 2 work).
In Lab 3 part 2 you write your own version of check_citations. This one is the reference logic from Demo 6."""
import re


def cited_ids(answer):
    return re.findall(r"\[(KB-\d+)\]", answer or "")


def check_citations(answer, retrieved_ids):
    cited = cited_ids(answer)
    if "not found" in (answer or "").lower():
        return "pass_not_found"
    if not cited:
        return "fail_no_citation"
    if any(c not in retrieved_ids for c in cited):
        return "fail_fake_citation"
    return "pass"
