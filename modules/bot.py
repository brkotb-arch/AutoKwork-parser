from loguru import logger
import os
TOKEN = os.environ.get("TOKEN")
USERID = os.environ.get("USERID")
import telebot
# telebot.apihelper.API_URL = "https://tg-proxy.brkotb.workers.dev"
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
# ========== ВСТАВЬ ЭТОТ БЛОК ПОСЛЕ ВСЕХ ИМПОРТОВ ==========
import threading
import os
from flask import Flask

# Создаем Flask-приложение для health check
flask_app = Flask(__name__)

@flask_app.route('/')
def health_check():
    return "Bot is alive!", 200

def run_flask():
    # Render сам подставит порт через переменную окружения PORT
    port = int(os.environ.get('PORT', 10000))
    flask_app.run(host='0.0.0.0', port=port, threaded=True)

# Запускаем Flask в отдельном потоке
flask_thread = threading.Thread(target=run_flask, daemon=True)
flask_thread.start()
# ========== КОНЕЦ БЛОКА ДЛЯ ВСТАВКИ ==========

# ... здесь создается твой бот: bot = telebot.TeleBot(TOKEN) ...

# ... здесь все твои обработчики (@bot.message_handler...) ...

if __name__ == '__main__':
    # Вместо bot.infinity_polling() может быть bot.polling()
    # Просто убедись, что строка не закомментирована и не удалена.
    print("🤖 Бот запущен!")
    bot.infinity_polling()  # <-- ЭТА СТРОЧКА У ТЕБЯ УЖЕ ЕСТЬ, НЕ УДАЛЯЙ ЕЁ

bot = telebot.TeleBot(TOKEN)

def send_order_notification(order):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton("🔗 Откликнуться", url=order['link'])
    keyboard.add(button)
    
    text = f"""🔔 НОВЫЙ ЗАКАЗ!
    
📌 {order['title']}

💰 {order['price']} ₽

👉 Нажми на кнопку, чтобы открыть заказ
"""
    bot.send_message(chat_id=USERID, text=text, reply_markup=keyboard)