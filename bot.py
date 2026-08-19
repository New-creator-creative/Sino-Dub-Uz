import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Sino Dub Uz botiga xush kelibsiz!\n\n"
        "Anime qidirish uchun foydalaning."
    )


def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise RuntimeError("BOT_TOKEN topilmadi!")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    print("Sino Dub Uz bot ishga tushdi!")
    app.run_polling()


if __name__ == "__main__":
    main()
