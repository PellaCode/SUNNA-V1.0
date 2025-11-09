import os
import re
from config import DOWNLOAD_DIR

def ensure_dirs():
    """
    ينشئ المجلدات الأساسية إذا لم تكن موجودة.
    يتأكد أن DOWNLOAD_DIR هو مجلد وليس ملف.
    """
    if os.path.exists(DOWNLOAD_DIR) and not os.path.isdir(DOWNLOAD_DIR):
        os.remove(DOWNLOAD_DIR)
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    os.makedirs("sessions", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

def is_url(text: str) -> bool:
    """
    يتحقق إذا كان النص عبارة عن رابط صالح.
    """
    return bool(re.match(r'https?://', text.strip()))

def format_duration(seconds: int) -> str:
    """
    يحول المدة الزمنية من ثواني إلى صيغة mm:ss أو hh:mm:ss.
    """
    if seconds < 60:
        return f"0:{seconds:02d}"
    elif seconds < 3600:
        minutes = seconds // 60
        sec = seconds % 60
        return f"{minutes}:{sec:02d}"
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        sec = seconds % 60
        return f"{hours}:{minutes:02d}:{sec:02d}"

def sanitize_filename(name: str) -> str:
    """
    ينظف اسم الملف من الرموز غير المسموح بها في أنظمة الملفات.
    """
    return re.sub(r'[\\/*?:"<>|]', "_", name).strip()

def get_file_size(path: str) -> str:
    """
    يعيد حجم الملف بصيغة مقروءة (KB, MB).
    """
    if not os.path.isfile(path):
        return "غير موجود"
    size = os.path.getsize(path)
    if size < 1024:
        return f"{size} B"
    elif size < 1024 * 1024:
        return f"{size // 1024} KB"
    else:
        return f"{size // (1024 * 1024)} MB"
