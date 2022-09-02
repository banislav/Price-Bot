import telebot
from config import token

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, i am a price bot')


bot.infinity_polling()
