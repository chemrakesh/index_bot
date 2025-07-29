# 📦 Import necessary modules from python-telegram-bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time
import os

# 🧠 This function runs when someone types "/index"
async def fear_greed(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 🌐 URL of the daily updated Fear & Greed Index image
    #image_url = "https://alternative.me/crypto/fear-and-greed-index.png"
    image_url = f"https://alternative.me/crypto/fear-and-greed-index.png?nocache={int(time.time())}"


    # 📤 Reply with the image to the user
    await update.message.reply_photo(photo=image_url)

# 🚀 Start the Telegram bot application
# Replace YOUR_BOT_TOKEN with the token from @BotFather
app = ApplicationBuilder().token("7983460811:AAH5hrJYXUgeOiv8zY9mkQYlKKUuXmO_NC4").build()

# 🔗 Link the "/index" command to our image sending function
app.add_handler(CommandHandler("index", fear_greed))

# Use webhook instead of polling
PORT = int(os.environ.get("PORT", 8080))
app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url="https://indexbot-chemrakesh9505-k31o2427.leapcell.dev/"
)
