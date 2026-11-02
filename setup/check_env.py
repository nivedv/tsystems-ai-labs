"""Run this first. It checks your settings and never prints your key."""
import os
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "lib"))
from common import REQUIRED, ROOT, load_env  # noqa: E402

load_env()
print(f".env file in repo root: {'found' if (ROOT / '.env').exists() else 'NOT FOUND'}")
ok = (ROOT / ".env").exists()
for k in REQUIRED:
    v = os.environ.get(k)
    if not v:
        print(f"[MISSING] {k}")
        ok = False
    elif k == "AZURE_OPENAI_API_KEY":
        print(f"[ set   ] {k}  (value hidden)")
    else:
        print(f"[ set   ] {k} = {v}")
for mod in ("openai", "jsonschema"):
    try:
        m = __import__(mod)
        print(f"[ ok    ] {mod} installed")
    except ImportError:
        print(f"[MISSING] {mod}  ->  pip install -r requirements.txt")
        ok = False
if ok:
    try:
        from common import get_client
        client, dep = get_client()
        r = client.chat.completions.create(model=dep, messages=[{"role": "user", "content": "Reply with the word OK."}])
        print(f"[ ok    ] test call worked. finish_reason={r.choices[0].finish_reason}")
    except Exception as e:
        print(f"[FAILED ] test call: {type(e).__name__}: {str(e)[:200]}")
        ok = False
print("\nREADY." if ok else "\nNot ready. Fix the lines above, or raise your hand.")
