"""Your tiny RAG toolkit. Lab 3 part 1 builds it. Lab 3 part 2, Lab 4 and the practice REUSE it.
Three functions to finish: load_kb (TODO 1), search (TODO 2), build_messages (TODO 3)."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "lib"))
import common  # noqa: E402
import textutils  # noqa: E402

KB_DIR = common.ROOT / "kb"
GROUND_RULE = "Answer ONLY from the articles. Cite IDs like [KB-004]. If missing, reply: not found."


def load_kb(kb_dir=KB_DIR):
    """Return a dict: article id -> article text, for example {"KB-001": "VPN will not connect from home. If the ..."}"""
    kb = {}
    for path in sorted(pathlib.Path(kb_dir).glob("KB-*.txt")):
        raw = path.read_text(encoding="utf-8")
        # TODO 1: the file has lines "ID: ...", "Title: ...", "Text: ...".
        #         Save "<title>. <text>" in kb[path.stem]   (path.stem is the article id, for example KB-004)
        pass
    return kb


def search(question, kb, k=2, min_score=0):
    """Return the top k articles as a list of (article_id, score), best first. Only scores >= min_score."""
    # TODO 2: score = how many DIFFERENT question words appear in the article.
    #         (textutils.words(text) gives the words of a text; sets help: q_words & article_words)
    #         Sort best score first; if scores are equal, smaller article id first.
    #         Keep only scores >= min_score. Return the first k as (article_id, score).
    return None


def build_messages(question, hits, kb):
    """Return the 2 messages for the model. hits is the list from search()."""
    # TODO 3: system message = GROUND_RULE.
    #         user message = the articles, each line like "[KB-004] <text>", then a blank line, then "Question: <question>"
    return None
