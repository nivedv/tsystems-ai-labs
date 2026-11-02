"""Small text helper for the RAG labs (provided, so you can focus on search and prompts).
words(text) -> list of lowercase words, without common filler words, with simple plural handling."""
import re

STOP = set("""a an the is are was were be been am i we you my our your it its this that to of in on at for from with
and or not do does did can could should would how what why when who which me us there their they them if as by so
please very more most some any about after before again""".split())


def words(s):
    out = []
    for w in re.findall(r"[a-z0-9]+", s.lower()):
        if w in STOP or len(w) < 2:
            continue
        if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
            w = w[:-1]
        out.append(w)
    return out
