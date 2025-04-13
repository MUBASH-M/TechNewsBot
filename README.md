# TechNewsBot

TechNewsBot is a Telegram bot that fetches and shares the latest technology news live using the NewsAPI. Users can interact with the bot directly in their Telegram chat to receive updates on the latest tech news.

## Features
- Fetches the latest technology news from NewsAPI.
- Shares news articles directly in Telegram chats.
- Interactive commands for users to customize their news feed.

## Setup Instructions

### Prerequisites
1. Python 3.8 or higher
2. A Telegram bot token (create one using the BotFather on Telegram).
3. A NewsAPI key (sign up at https://newsapi.org/ to get your API key).

### Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd TechNewsBot
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration
1. Create a `.env` file in the root directory and add the following:
   ```env
   TELEGRAM_BOT_TOKEN=<your-telegram-bot-token>
   NEWSAPI_KEY=<your-newsapi-key>
   ```

### Running the Bot
Run the bot using the following command:
```bash
python src/bot.py
```

## Project Structure

The project is organized as follows:

```
TechNewsBot/
├── README.md
├── requirements.txt
├── src/
│   ├── bot.py                # Main bot logic
│   ├── news_api.py           # Handles interactions with the NewsAPI
│   ├── commands/             # Contains bot command handlers
│   │   ├── latest_news.py    # Command to fetch the latest news
│   │   ├── start.py          # Command to start the bot
│   ├── utils/                # Utility modules
│   │   ├── logger.py         # Logging utilities
```

## Recent Updates

- Added modular command handlers under `src/commands/` for better scalability.
- Introduced a `logger.py` utility in `src/utils/` for improved logging and debugging.

## Usage

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the bot:
   ```bash
   python src/bot.py
   ```
