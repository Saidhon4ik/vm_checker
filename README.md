# vm_checker
# 🖥️ VM Checker Bot

A Telegram bot that monitors your Linux server stats in real time.

## Features

- `/start` — Welcome message + available commands
- `/uptime` — Server uptime
- `/memory` — RAM usage
- `/disk` — Disk usage

## Access Control

Only your Telegram ID can use this bot. Set `MY_ID` in `bot.py` to your Telegram ID.  
To find your ID — message [@userinfobot](https://t.me/userinfobot) on Telegram.

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/Saidhon4ik/vm_checker.git
cd vm_checker
```

### 2. Install dependencies
```bash
pip install python-telegram-bot python-dotenv --break-system-packages
```

### 3. Create `.env` file
```
TELEGRAM_TOKEN=your_token_here
```

### 4. Run the bot
```bash
nohup python3 bot.py &
```

## Tech Stack

- Python 3
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- `subprocess` — executes Linux shell commands
- `python-dotenv` — loads token from `.env`

## Deployment

Runs on a GCP Compute Engine VM (e2-micro) 24/7 via `nohup`.
