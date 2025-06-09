from telegram.ext import ApplicationBuilder, MessageHandler, CallbackQueryHandler, filters
from handlers.messages import handle_user_prompt
from handlers.callbacks import handle_doc_buttons
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build the Telegram bot application
app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

# Register handlers for text and button callbacks
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_user_prompt))
app.add_handler(CallbackQueryHandler(handle_doc_buttons))

# Start the bot
if __name__ == "__main__":
    print("🤖 QA AI Bot is running...")
    app.run_polling()
