
import os
import yt_dlp
from config import DOWNLOAD_DIR, YTDLP_COOKIES, YTDLP_USER_AGENT

def _build_headers():
    return {'User-Agent': YTDLP_USER_AGENT} if YTDLP_USER_AGENT else {}

def download_audio(url: str) -> str:
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(id)s.%(ext)s'),
        'cookies': YTDLP_COOKIES,
        'http_headers': _build_headers(),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return os.path.join(DOWNLOAD_DIR, f"{info['id']}.mp3")

def build_ffmpeg_live_cmd(url: str, sample_rate: int = 48000, channels: int = 2) -> str:
    return (
        f"ffmpeg -hide_banner -loglevel warning -re -i \"{url}\" "
        f"-vn -acodec pcm_s16le -f s16le -ac {channels} -ar {sample_rate} pipe:1"
    )
