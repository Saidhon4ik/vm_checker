# type: ignore
import os
import subprocess
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()
TOKEN = os.environ.get("TELEGRAM_TOKEN")
MY_ID = 123456789  # replace with your Telegram ID (integer)

def check_access(update: Update) -> bool:
    return update.message.chat_id == MY_ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_access(update):
        await update.message.reply_text("No access!")
        return
    await update.message.reply_text("Hi! I am your server assistant 🖥️\n/uptime /memory /disk")

async def uptime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_access(update):
        await update.message.reply_text("No access!")
        return
    result = subprocess.run("uptime", capture_output=True, text=True)
    await update.message.reply_text(f"⏱ Uptime:\n{result.stdout}")

async def memory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_access(update):
        await update.message.reply_text("No access!")
        return
    result = subprocess.run(["free", "-m"], capture_output=True, text=True)
    await update.message.reply_text(f"💾 Memory:\n{result.stdout}")

async def disk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_access(update):
        await update.message.reply_text("No access!")
        return
    result = subprocess.run(["df", "-h"], capture_output=True, text=True)
    await update.message.reply_text(f"💿 Disk:\n{result.stdout}")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("uptime", uptime))
app.add_handler(CommandHandler("memory", memory))
app.add_handler(CommandHandler("disk", disk))
print("Server bot is running...")
app.run_polling()