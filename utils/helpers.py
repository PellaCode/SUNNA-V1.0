import os
from config import DOWNLOAD_DIR

def ensure_dirs():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    os.makedirs("sessions", exist_ok=True)
    os.makedirs("assets/thumbnails", exist_ok=True)

def is_url(text: str) -> bool:
    return text.startswith("http://") or text.startswith("https://")
