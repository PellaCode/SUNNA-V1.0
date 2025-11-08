import os
from ntgcalls.types import AudioPiped, MediaStream, AudioFrame
from utils.youtube import build_ffmpeg_live_cmd
from config import AUDIO_SAMPLE_RATE, AUDIO_CHANNELS

class AudioController:
    def __init__(self, ntg):
        self.ntg = ntg

    async def play_file(self, chat_id: int, file_path: str):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"الملف غير موجود: {file_path}")
        await self.ntg.join_group_call(chat_id, AudioPiped(file_path))

    async def play_live(self, chat_id: int, url: str):
        ffmpeg_cmd = build_ffmpeg_live_cmd(url, AUDIO_SAMPLE_RATE, AUDIO_CHANNELS)
        await self.ntg.join_group_call(chat_id, MediaStream(ffmpeg_cmd))

    async def stop(self, chat_id: int):
        await self.ntg.leave_group_call(chat_id)

    async def send_frame(self, chat_id: int, pcm_bytes: bytes):
        frame = AudioFrame(pcm_bytes, sample_rate=AUDIO_SAMPLE_RATE, channels=AUDIO_CHANNELS)
        await self.ntg.send_audio_frame(chat_id, frame)
