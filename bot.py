import threading
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from cloudways import run_selenium  # Import Selenium function

# Hardcoded Bot Credentials
BOT_TOKEN = "7379441276:AAHRk9qZGBl1rIoZhAiUcCH9ZPqjmbGpIbk"
ADMIN_ID = 5759284972  # Replace with your Telegram ID

bot = Bot(token=BOT_TOKEN)

def send_message(chat_id, text):
    """Send a message via Telegram bot."""
    bot.send_message(chat_id=chat_id, text=text)

def start(update: Update, context: CallbackContext):
    """Start command."""
    update.message.reply_text("👋 Bhai! Cloudways account banane ke liye `/create_cloudways email password` use kar!")

def create_account(update: Update, context: CallbackContext):
    """Handle /create_cloudways command."""
    if update.message.chat_id != ADMIN_ID:
        update.message.reply_text("🚫 Bhai sirf admin use kar sakta hai!")
        return

    if len(context.args) != 2:
        update.message.reply_text("⚠️ Format sahi likh bhai: `/create_cloudways email password`")
        return

    email = context.args[0]
    password = context.args[1]
    update.message.reply_text(f"🔄 Cloudways account bana raha hu for: {email}")

    # Run Selenium script in a separate thread
    thread = threading.Thread(target=run_selenium, args=(email, password, update.message.chat_id))
    thread.start()

def main():
    """Start the Telegram bot."""
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("create_cloudways", create_account))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()