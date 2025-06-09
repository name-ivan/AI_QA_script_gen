# 🤖 QA AI Bot – Generate Test Docs with Claude 3 Sonnet

This is a Telegram bot that uses **Claude 3 Sonnet** (via Anthropic API) to generate QA documentation from user-written prompts.

You can:
- 🧠 Write a product description or user story over several messages
- 🎛️ Choose what you want to generate:
  - 🧪 Test Stories
  - 🧾 Test Suite
  - ☑️ Checklist
  - 🐞 Bug Report
- 📄 Get the result directly in Telegram chat

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/qa_ai_bot.git
cd qa_ai_bot
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your secrets to `.env`

Create a `.env` file in the root folder:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
ANTHROPIC_API_KEY=your_claude_api_key_here
```

> ⚠️ Make sure `.env` is listed in `.gitignore`.

---

## ▶️ Running the Bot

```bash
python main.py
```

---

## 🧪 How to Use It

1. Open your bot in Telegram (e.g. `@QAhelper_AI_bot`)
2. Type your prompt in 1 or more messages (e.g. product feature description)
3. Click one of the buttons:
   - 🧪 Test Stories
   - 🧾 Test Suite
   - ☑️ Checklist
   - 🐞 Bug Report
4. The bot will generate the requested QA document using Claude 3 Sonnet

---

## 🧠 Powered By

- 🧠 **Claude 3 Sonnet** via [Anthropic API](https://docs.anthropic.com)
- 🤖 **python-telegram-bot v22**
- ☁️ `.env` config via `python-dotenv`

---

## 📁 Project Structure

```plaintext
qa_ai_bot/
├── main.py
├── .env.example
├── requirements.txt
│
├── handlers/
│   ├── messages.py        # User input + buttons
│   └── callbacks.py       # Button logic & response
│
├── ai/
│   └── doc_generator.py   # Claude 3 logic via Anthropic API
```

---

## ✅ To Do

- [ ] Save output to Google Docs or Sheets
- [ ] Add "Regenerate" or "Refine" prompt options
- [ ] Auto-generate Selenium test code
