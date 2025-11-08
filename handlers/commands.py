from pyrogram import filters
from utils.helpers import is_url
from utils.redis_client import push_command

def register_command_handlers(app):
    @app.on_message(filters.command("play"))
    async def play_handler(client, message):
        if len(message.command) < 2:
            return await message.reply("❗ استخدم: /play <مسار ملف أو رابط>")
        arg = message.text.split(" ", 1)[1]
        push_command("PLAY", message.chat.id, arg)
        await message.reply("✅ تم إرسال أمر التشغيل إلى الحساب المساعد.")

    @app.on_message(filters.command("stop"))
    async def stop_handler(client, message):
        push_command("STOP", message.chat.id)
        await message.reply("⏹️ تم إرسال أمر الإيقاف إلى الحساب المساعد.")
