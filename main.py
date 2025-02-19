# main.py
from telegram.ext import Updater, CommandHandler
from apscheduler.schedulers.background import BackgroundScheduler
from config import TOKEN, REMINDER_TIME
from handlers import start
from database import init_db, send_reminder  # send_reminder мы реализуем ниже

def main():
    # Инициализация базы данных
    init_db()

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Регистрируем команду /start
    dp.add_handler(CommandHandler("start", start))

    # Настройка планировщика напоминаний
    scheduler = BackgroundScheduler()
    hour, minute = REMINDER_TIME.split(":")
    scheduler.add_job(lambda: send_reminder(updater.bot),
                      'cron', hour=hour, minute=minute)
    scheduler.start()

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
