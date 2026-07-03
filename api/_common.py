import os
import json
from typing import Optional

API_KEYS = {}


def load_env():
    for line in open(".env", "r"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ[k.strip()] = v.strip()


def get_api_key(name: str) -> Optional[str]:
    return os.environ.get(f"{name}_API_KEY") or API_KEYS.get(name)
