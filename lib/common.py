"""Shared helpers for all labs. Reads settings from environment variables or the .env file in the repo root.
No script in this repo ever prints the API key."""
import os
import pathlib
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQUIRED = [
    "AZURE_OPENAI_ENDPOINT",
    "AZURE_OPENAI_API_KEY",
    "AZURE_OPENAI_API_VERSION",
    "AZURE_OPENAI_DEPLOYMENT",
]


def load_env():
    p = ROOT / ".env"
    if not p.exists():
        return
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def missing_settings():
    load_env()
    return [k for k in REQUIRED if not os.environ.get(k)]


def get_client():
    miss = missing_settings()
    if miss:
        print("Missing settings:", ", ".join(miss))
        print("Put the .env file from your trainer in the repo root, then run:  python setup/check_env.py")
        sys.exit(2)
    from openai import AzureOpenAI

    client = AzureOpenAI(
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    )
    return client, os.environ["AZURE_OPENAI_DEPLOYMENT"]


HINTS = {
    "AuthenticationError": "401: the key is wrong or not loaded. Is the .env file in the repo root?",
    "PermissionDeniedError": "403: the key is valid but not allowed. Ask your trainer.",
    "NotFoundError": "404: usually the DEPLOYMENT name is wrong. Check the .env file.",
    "RateLimitError": "429: too many requests. Wait 30 seconds and run again. Use a bigger --pause.",
    "APIConnectionError": "Network problem: check your internet / VPN, and the endpoint in .env.",
    "BadRequestError": "400: a setting is not accepted (for example temperature on some models). Read the message.",
    "APITimeoutError": "Timeout: run again.",
}


def explain_error(e):
    name = type(e).__name__
    print(f"\nCALL FAILED: {name}")
    print(str(e)[:400])
    print("Hint:", HINTS.get(name, "Read the message above, then check .env (endpoint, key, deployment, API version)."))


def call_model(client, deployment, messages, **extra):
    t0 = time.time()
    resp = client.chat.completions.create(model=deployment, messages=messages, **extra)
    return resp, time.time() - t0
