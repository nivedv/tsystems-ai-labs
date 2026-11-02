"""Run this FIRST in Lab 1 (one call). It tells you whether your deployment accepts the temperature setting.
If it does not, use the fallback:  lab1_variance.py --mode wording"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "lib"))
import common  # noqa: E402

client, deployment = common.get_client()
try:
    common.call_model(client, deployment, [{"role": "user", "content": "Reply with the word OK."}], temperature=0.7)
    print("Temperature is ACCEPTED. Use the normal mode:  --mode temperature")
except Exception as e:
    print(f"Temperature was NOT accepted ({type(e).__name__}).")
    print(str(e)[:300])
    print("Use the fallback:  --mode wording   (same ticket, three prompt wordings, five runs each)")
