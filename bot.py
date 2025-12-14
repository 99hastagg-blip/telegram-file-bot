import os
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("✅ Bot is running!\nSend me any file.")

def file_handler(update, context):
    file = update.message.document or update.message.video or update.message.audio
    if not file:
        return
    file_id = file.file_id
    bot_username = context.bot.username
    link = f"https://t.me/{bot_username}?start={file_id}"
    update.message.reply_text(f"📁 File link:\n{link}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.document | Filters.video | Filters.audio, file_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
