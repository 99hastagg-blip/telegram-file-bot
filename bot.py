from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8204485442:AAHcwbEMRy3t6RY-UXyvLeeSwa8YNh7QZ4k"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 File bhejo, main link bana dunga")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document or update.message.video or update.message.audio
    if not file:
        return

    file_id = file.file_id
    bot_username = context.bot.username
    link = f"https://t.me/{bot_username}?start={file_id}"
    await update.message.reply_text(f"✅ File link:\n{link}")

async def deep_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        file_id = context.args[0]
        await context.bot.send_document(chat_id=update.effective_chat.id, document=file_id)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("start", deep_link))
app.add_handler(MessageHandler(filters.Document.ALL | filters.Video.ALL | filters.Audio.ALL, handle_file))

app.run_polling()
