from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "7964768911:AAEhuV6B-vmwJpdJhnbguSqTyBX5_5tjXLQ"

async def auto_delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.delete()

app = ApplicationBuilder().token(TOKEN).build()

# Faqat URL larni o'chiradi
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(r'https?://'), auto_delete))

print("Bot ishlayapti...")
app.run_polling()