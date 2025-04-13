from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from src.commands.start import start_command
from src.commands.latest_news import latest_news_command

# Initialize the bot application
app = ApplicationBuilder().token(os.environ['TELEGRAM_BOT_TOKEN']).build()

# Register command handlers
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("latest", latest_news_command))

# Start the bot
if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()
