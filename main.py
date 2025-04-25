
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

workout_data = {
    "strength": ["Push-ups", "Squats", "Deadlifts", "Bench Press"],
    "cardio": ["Running", "Jump Rope", "Cycling", "Swimming"],
    "flexibility": ["Yoga", "Stretching", "Pilates"]
}

reply_keyboard = [["Strength", "Cardio", "Flexibility"]]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Выбери тип тренировки:", reply_markup=markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.lower()
    exercises = workout_data.get(user_input, None)
    if exercises:
        await update.message.reply_text(f"Вот несколько упражнений для {user_input}:
- " + "\n- ".join(exercises))
    else:
        await update.message.reply_text("Пожалуйста, выбери один из предложенных типов.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
