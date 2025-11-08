# SUNNA V1.0 - البوت الرسمي
# يستقبل الأوامر من المستخدمين ويخزنها في Redis ليقوم الحساب المساعد بتنفيذها

from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME, WELCOME_IMAGE
from utils.helpers import ensure_dirs, is_url
from utils.redis_client import push_command
from handlers.commands import register_command_handlers
from handlers.callbacks import register_callback_handlers
from utils.logger import setup_logger

log = setup_logger()

# إنشاء عميل البوت الرسمي
app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# تسجيل الأوامر
register_command_handlers(app)
register_callback_handlers(app)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    """رسالة ترحيب عند بدء البوت"""
    await message.reply_photo(
        photo=WELCOME_IMAGE,
        caption=(
            "👋 مرحبًا بك في SUNNA V1.0\n\n"
            "🎶 بوت تشغيل الدروس السلفية داخل القنوات والمجموعات.\n"
            "يدعم الملفات المحلية وروابط YouTube، ويعمل مع حساب مساعد عبر Redis.\n\n"
            "🛠️ الأوامر:\n"
            "• /play <رابط أو مسار> لتشغيل مباشر\n"
            "• /stop لإيقاف التشغيل\n"
            "• /queue <رابط أو مسار> لإضافة للقائمة\n"
            "• /next لتشغيل التالي\n"
            "• /list لعرض قائمة الانتظار\n"
        )
    )

@app.on_message(filters.command("queue"))
async def queue_handler(client, message):
    """إضافة عنصر إلى قائمة الانتظار"""
    if len(message.command) < 2:
        return await message.reply("❗ استخدم: /queue <رابط أو مسار>")
    arg = message.text.split(" ", 1)[1].strip()
    push_command("QUEUE", message.chat.id, arg)
    await message.reply("✅ تمت إضافة العنصر إلى قائمة الانتظار.")

@app.on_message(filters.command("next"))
async def next_handler(client, message):
    """تشغيل العنصر التالي من قائمة الانتظار"""
    push_command("NEXT", message.chat.id)
    await message.reply("⏭️ تم إرسال أمر تشغيل التالي إلى الحساب المساعد.")

@app.on_message(filters.command("list"))
async def list_handler(client, message):
    """عرض قائمة الانتظار (تنفيذ مستقبلي من الحساب المساعد)"""
    push_command("LIST", message.chat.id)
    await message.reply("📋 تم طلب عرض قائمة الانتظار من الحساب المساعد.")

# بدء التشغيل
def main():
    ensure_dirs()
    log.info("🚀 بدء تشغيل SUNNA V1.0 (البوت الرسمي)...")
    app.run()

if __name__ == "__main__":
    main()
