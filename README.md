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
```
TechNewsBot/
├── README.md
├── requirements.txt
├── .env.example
├── src/
│   ├── bot.py
│   ├── news_api.py
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── start.py
│   │   ├── latest_news.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
└── tests/
    ├── test_news_api.py
    ├── test_bot.py
```

## License
This project is licensed under the MIT License.
