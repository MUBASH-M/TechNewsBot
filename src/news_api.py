from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Example usage of TELEGRAM_BOT_TOKEN if required
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

def fetch_news_by_category(category):
    """Fetch news by category using the News API."""
    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        raise ValueError("NEWS_API_KEY is not set in the environment variables.")

    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "category": category,
        "apiKey": api_key,
        "language": "en",
        "country": "us"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        raise Exception(f"Failed to fetch news: {response.status_code} {response.text}")
