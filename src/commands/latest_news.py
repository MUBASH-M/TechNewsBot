from telegram import Update
from telegram.ext import ContextTypes
from src.news_api import fetch_latest_technology_news

async def latest_news_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        articles = fetch_latest_technology_news()
        if not articles:
            await update.message.reply_text("No technology news available at the moment.")
            return

        for article in articles[:5]:  # Limit to 5 articles
            title = article.get("title")
            url = article.get("url")
            await update.message.reply_text(f"{title}\n{url}")
    except Exception as e:
        await update.message.reply_text("Failed to fetch news. Please try again later.")
        print(f"Error: {e}")
