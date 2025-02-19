# handlers.py
from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    welcome_text = (
        f"Привет, {user.first_name}!\n"
        "Я бот для поддержки ЛФК при артрите. Я буду напоминать тебе о выполнении упражнений и помогать отслеживать твое самочувствие.\n"
        "Пожалуйста, оцени своё текущее самочувствие от 1 до 10."
    )
    update.message.reply_text(welcome_text)
    # Здесь можно добавить код для сохранения пользователя в базу данных.





# Добавьте в handlers.py
import sqlite3
from config import DATABASE

def send_reminder(bot):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT user_id FROM users")
    users = c.fetchall()
    for (user_id,) in users:
        bot.send_message(chat_id=user_id, text="Напоминаю, пора выполнять ЛФК! Введите /exercise для получения инструкций.")
    conn.close()
