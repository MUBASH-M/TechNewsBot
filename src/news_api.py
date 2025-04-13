from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Example usage of TELEGRAM_BOT_TOKEN if required
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# ...existing code...
