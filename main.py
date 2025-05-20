import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

def get_keyboard():
    return ReplyKeyboardMarkup([
        ["🔢 حساب المعدل"],
        ["📱 تواصل معنا"]
    ], resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 مرحباً بك! اختر من القائمة:", reply_markup=get_keyboard())

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text

    if msg == "🔢 حساب المعدل":
        await update.message.reply_text(
            "أرسل المعلومات بهذا الشكل:\n"
            "المعدل: 3.5\n"
            "المنجزة: 60\n"
            "المتبقية: 30\n"
            "النظام: 5",
            reply_markup=get_keyboard()
        )

    elif msg == "📱 تواصل معنا":
        await update.message.reply_text(
            "تواصل معنا عبر:\n"
            "• TikTok: @ohood_ow20\n"
            "• Snapchat: ohood_ow20\n"
            "• X: @ohood_ow20",
            reply_markup=get_keyboard()
        )

    elif all(x in msg for x in ["المعدل", "المنجزة", "المتبقية"]):
        try:
            lines = msg.split('\n')
            gpa = float(lines[0].split(':')[1])
            done = int(lines[1].split(':')[1])
            remaining = int(lines[2].split(':')[1])
            system = int(lines[3].split(':')[1])

            max_gpa = ((gpa * done) + (system * remaining)) / (done + remaining)
            await update.message.reply_text(
                f"📊 أقصى معدل ممكن: {round(max_gpa, 2)}",
                reply_markup=get_keyboard()
            )
        except:
            await update.message.reply_text("⚠️ الرجاء إدخال المعلومات بالشكل الصحيح", reply_markup=get_keyboard())

    else:
        await update.message.reply_text("❓ اختر من القائمة", reply_markup=get_keyboard())

def main():
    app = Application.builder().token(os.environ["BOT_TOKEN"]).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
