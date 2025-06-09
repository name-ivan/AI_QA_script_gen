from telegram import Update
from telegram.ext import ContextTypes
from ai.doc_generator import generate_doc
from .messages import prompt_buffer

async def handle_doc_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat.id
    await query.answer()

    # Get accumulated prompt text
    prompt = "\n".join(prompt_buffer.get(chat_id, []))
    doc_type = query.data.replace("gen_", "")

    await query.edit_message_text(f"🧠 Generating {doc_type.replace('_', ' ').title()}...")

    try:
        # Call AI to generate documentation
        output = generate_doc(prompt, doc_type)

        # Send the output back to the user
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"📄 *{doc_type.replace('_', ' ').title()}*:\n\n{output}",
            parse_mode="Markdown"
        )

        # Clear the buffer for next prompt session
        prompt_buffer[chat_id] = []

    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"⚠️ Error generating document: {e}")
