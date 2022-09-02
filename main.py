import telebot
from config import token
from scraping.mvideo_parser import MvideoParser

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, i am a price bot')

if __name__ == '__main__':
    # bot.infinity_polling()
    instance = MvideoParser()
    print(instance.find_price("iphone 13"))