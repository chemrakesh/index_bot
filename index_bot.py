import os
import time
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def fear_greed(update, context: ContextTypes.DEFAULT_TYPE):
    image_url = f"https://alternative.me/crypto/fear-and-greed-index.png?nocache={int(time.time())}"
    await update.message.reply_photo(photo=image_url)

app = ApplicationBuilder().token("BOT_TOKEN").build()
app.add_handler(CommandHandler("index", fear_greed))

PORT = int(os.environ.get("PORT", 8080))
app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url="https://indexbot-chemrakesh9505-k31o2427.leapcell.dev/"
)
