from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# A buffer to collect message parts from each user by chat_id
prompt_buffer = {}

async def handle_user_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message_text = update.message.text.strip()

    # Save message into buffer
    if chat_id not in prompt_buffer:
        prompt_buffer[chat_id] = []
    prompt_buffer[chat_id].append(message_text)

    # Buttons for user to choose what kind of doc to generate
    keyboard = [
        [InlineKeyboardButton("🧪 Test Stories", callback_data="gen_test_stories")],
        [InlineKeyboardButton("🧾 Test Suite", callback_data="gen_test_suite")],
        [InlineKeyboardButton("☑️ Checklist", callback_data="gen_checklist")],
        [InlineKeyboardButton("🐞 Bug Report", callback_data="gen_bug_report")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Reply with confirmation + buttons
    await update.message.reply_text(
        "📝 Prompt received. What do you want to generate?",
        reply_markup=reply_markup
    )
