# 🧠 Nick Background Remover Bot

A simple **Telegram bot** that removes image backgrounds automatically using the [remove.bg API](https://www.remove.bg/api).  
Built using **Python** and the **python-telegram-bot** library.

---

## 🚀 Features

- Removes the background from any photo sent to the bot  
- Uses the `remove.bg` API for accurate background removal  
- Sends back the processed image with the background removed  

---

## 🧩 Requirements

Before running the bot, make sure you have:

- Python 3.8 or above  
- A Telegram Bot Token (from [BotFather](https://t.me/BotFather))  
- An API key from [remove.bg](https://www.remove.bg/api#remove-background)

---

## 🤖 How to Create a Telegram Bot using BotFather

1. Open Telegram and search for **@BotFather**.
2. Start a chat with BotFather and type:
   /start
3. Create a new bot:
  /newbot
4. Follow the prompts to:
- Enter a bot name (e.g., Nick Background Remover)
- Enter a bot username (must end with `_bot`, e.g., `NickBgRemover_bot`)
5. BotFather will give you a **Bot Token**, which looks like:
  "1234567890:ABCdefGhIJKlmNoPQRstuVWXyz123456789"
6. Copy this token — you’ll need it later.

---

## 🔑 Get Your remove.bg API Key

1. Go to [remove.bg API](https://www.remove.bg/api).
2. Sign up or log in.
3. Copy your **API Key** — you’ll use it in the code.

---

## 🧱 Setting Up the Project

### 1. Clone or Download the Project

```
git clone https://github.com/yourusername/nick-bg-remover-bot.git
cd nick-bg-remover-bot
```
### Create a Virtual Environment
Create a new virtual environment (recommended to isolate dependencies):
  python -m venv venv
- Activate it:
    Windows:
      venv\Scripts\activate
    Mac/Linux:
      source venv/bin/activate
---

### Install Dependencies
pip install python-telegram-bot==20.3 requests

---

### Add your API Key
Open OPen the python fileand replace the placeholders:
  TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
  REMOVE_BG_API_KEY = "YOUR_REMOVE_BG_API_KEY"

---

### RUN The Bot
Once everything is set up, start your bot by running:
    Python bot.py

---

### Optional: Deactivate the Virtual Environment
deactivate

---

Developed by: Nitish Gharde
💬 Telegram: @TaskingNicksBot


