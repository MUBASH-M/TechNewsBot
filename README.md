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
### Installation (continued)
2. Navigate to the project directory:
   ```bash
   cd TechNewsBot
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration
1. Create a `.env` file in the root directory and add the following:
   ```env
   TELEGRAM_BOT_TOKEN=<your-telegram-bot-token>
   NEWSAPI_KEY=<your-newsapi-key>
   ```

### Usage
1. Start the bot by running the following command:
   ```bash
   python src/bot.py
   ```
2. Interact with the bot on Telegram using the following commands:
   - `/latest_news` - Fetch the latest technology news.
   - `/start` - Start interacting with the bot.
   - `/tag <keyword>` - Get news articles related to a specific keyword.

### Project Structure
```
TechNewsBot/
├── README.md
├── requirements.txt
├── src/
│   ├── bot.py          # Main bot script
│   ├── news_api.py     # Handles interactions with NewsAPI
│   ├── commands/       # Contains bot command scripts
│   │   ├── latest_news.py
│   │   ├── start.py
│   │   └── tag.py
│   └── utils/          # Utility scripts
│       └── logger.py   # Logging utility
```

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
