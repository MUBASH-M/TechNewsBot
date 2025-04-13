import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

if not NEWSAPI_KEY:
    raise ValueError("NEWSAPI_KEY is not set in the environment variables.")

def fetch_latest_technology_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "category": "technology",
        "apiKey": NEWSAPI_KEY,
        "language": "en",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        response.raise_for_status()
