from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import re
import os

TOKEN = os.getenv("TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.strip()
    match = re.match(r"^([+-])(\d+)$", message)
    if match:
        operator = match.group(1)
        amount = match.group(2)
        if operator == "+":
            reply = f"Saldo berhasil **ditambahkan** sebesar {amount}"
        else:
            reply = f"Saldo berhasil **dikurangi** sebesar {amount}"
        await update.message.reply_text(reply, parse_mode="Markdown")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("Bot is running...")
    app.run_polling()
