import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from src.commands.start import start_command
from src.commands.latest_news import latest_news_command

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set in the environment variables.")

# Initialize the bot application
app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

# Register command handlers
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("latest", latest_news_command))

# Start the bot
if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()
