# SUNNA V1.0 - الحساب المساعد
# ينفذ أوامر التشغيل القادمة من البوت الرئيسي عبر Redis

import asyncio
from pyrogram import Client
from ntgcalls import NtgCalls
from ntgcalls.types import AudioPiped, MediaStream
from config import API_ID, API_HASH, SESSION_STRING
from utils.redis_client import pop_command
from utils.youtube import build_ffmpeg_live_cmd
from utils.logger import setup_logger

log = setup_logger()

# إنشاء عميل الحساب المساعد
assistant = Client("assistant", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)
ntg = NtgCalls(assistant)

async def command_listener():
    """مراقبة Redis وتنفيذ الأوامر تلقائيًا"""
    while True:
        cmd_data = pop_command()
        if cmd_data:
            cmd, chat_id, arg = cmd_data
            log.info(f"📥 أمر مستلم: {cmd} | الدردشة: {chat_id} | الوسيط: {arg}")

            try:
                if cmd == "PLAY":
                    if arg.startswith("http"):
                        ffmpeg_cmd = build_ffmpeg_live_cmd(arg)
                        await ntg.join_group_call(chat_id, MediaStream(ffmpeg_cmd))
                        log.info("✅ تم تشغيل البث المباشر عبر MediaStream")
                    else:
                        await ntg.join_group_call(chat_id, AudioPiped(arg))
                        log.info("✅ تم تشغيل الملف الصوتي عبر AudioPiped")

                elif cmd == "STOP":
                    await ntg.leave_group_call(chat_id)
                    log.info("⏹️ تم إيقاف البث")

                elif cmd == "QUEUE":
                    # يمكن تخزين قائمة انتظار مستقبلًا
                    log.info("📌 تم استقبال عنصر لقائمة الانتظار (غير مفعل بعد)")

                elif cmd == "NEXT":
                    # يمكن تنفيذ تشغيل التالي مستقبلًا
                    log.info("⏭️ تم استقبال أمر تشغيل التالي (غير مفعل بعد)")

                elif cmd == "LIST":
                    # يمكن إرسال قائمة الانتظار مستقبلًا
                    log.info("📋 تم استقبال أمر عرض القائمة (غير مفعل بعد)")

            except Exception as e:
                log.error(f"❌ خطأ أثناء تنفيذ الأمر: {e}")

        await asyncio.sleep(1)  # تحقق كل ثانية

async def main():
    await assistant.start()
    await ntg.start()
    log.info("🚀 الحساب المساعد يعمل الآن وينتظر الأوامر...")
    asyncio.create_task(command_listener())
    await assistant.idle()

if __name__ == "__main__":
    asyncio.run(main())
