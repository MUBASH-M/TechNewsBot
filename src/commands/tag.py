from telegram import Update
from telegram.ext import ContextTypes

async def tag_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Extract the tag from the command arguments
        if context.args:
            tag = context.args[0].lower()
            await update.message.reply_text(f"You searched for the tag: {tag}")
        else:
            await update.message.reply_text("Please provide a tag to search for.")
    except Exception as e:
        await update.message.reply_text("Failed to process the tag command. Please try again later.")
        print(f"Error: {e}")
