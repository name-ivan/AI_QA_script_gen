# 🤖 QA AI Bot – Generate Test Docs with Claude 3 Haiku

This is a Telegram bot that uses **Claude 3 Haiku** (via Anthropic API) to generate QA documentation from user-written prompts.

You can:
- ✍️ Write a product description or user story over multiple messages
- 🎛️ Click a button to generate:
  - 🧪 Test Stories
  - 🧾 Test Suite
  - ☑️ Checklist
  - 🐞 Bug Report
- 📄 Get the result directly in the Telegram chat

- ## ▶️ How to Use the Bot

1. Go to Telegram and open [@QAhelper_AI_bot](https://t.me/QAhelper_AI_bot)
2. Type your test prompt in one or more messages
3. Choose what to generate using the button menu:
   - 🧪 Test Stories
   - 🧾 Test Suite
   - ☑️ Checklist
   - 🐞 Bug Report
4. The bot will respond using Claude 3 Haiku model

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

> ⚠️ Be sure `.env` is listed in `.gitignore`.

---

## ▶️ Running the Bot

```bash
python main.py
```

---

## 🧪 How to Use It

1. Open your bot in Telegram (e.g. `@QAhelper_AI_bot`)
2. Type your test prompt in one or more messages (e.g. “Login page with 2FA and forgot password”)
3. Click one of the buttons:
   - 🧪 Test Stories
   - 🧾 Test Suite
   - ☑️ Checklist
   - 🐞 Bug Report
4. The bot will use **Claude 3 Haiku** to generate the requested doc

---

## 🧠 Powered By

- 🤖 **Claude 3 Haiku** via [Anthropic API](https://docs.anthropic.com)
- 💬 **python-telegram-bot v22**
- ⚙️ `.env` configuration via `python-dotenv`

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
│   └── doc_generator.py   # Claude 3 API interaction
```

---

## ✅ To Do

- [ ] Save generated documents to:
  - Google Docs (for test stories, bug reports)
  - Google Sheets (for checklists, test cases)
- [ ] Generate Selenium-based test automation framework from test stories:
  - Create `pytest` test functions with Selenium boilerplate
  - Scaffold project structure (`tests/`, `conftest.py`, etc.)
  - Export as a zip or push to GitHub repo
- [ ] Generate manual test suites in table format:
  - Columns: Test Case ID, Description, Steps, Expected Result, Priority
  - Export as CSV or Google Sheet
- [ ] Add option to download generated test suite or framework locally
- [ ] Add "Regenerate" or "Refine" button to iterate on outputs
