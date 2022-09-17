import telebot

from config import TOKEN
from scraping.technopark_parser import TechnoparkParser
from scraping.creditasia_parser import CreditAsiaParser


bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, i am a price bot')

if __name__ == '__main__':
    # bot.infinity_polling()
    instance = TechnoparkParser()
    print(instance.get_product_list("iphone 13")[0])