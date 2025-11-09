import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_STRING = os.getenv("SESSION_STRING")

DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR", "downloads")
SESSION_NAME = os.getenv("SESSION_NAME", "sunna_bot")

# رابط مباشر لصورة PNG متوافقة مع Telegram
WELCOME_IMAGE = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Audio_play_icon.png/600px-Audio_play_icon.png"

YTDLP_COOKIES = os.getenv("YTDLP_COOKIES") or None
YTDLP_USER_AGENT = os.getenv("YTDLP_USER_AGENT")

AUDIO_CHANNELS = int(os.getenv("AUDIO_CHANNELS", 2))
AUDIO_SAMPLE_RATE = int(os.getenv("AUDIO_SAMPLE_RATE", 48000))
