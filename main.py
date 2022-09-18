import telebot
from telebot import types

import configuration.config as cfg
from scraping.technopark_parser import TechnoparkParser
from scraping.creditasia_parser import CreditAsiaParser


bot = telebot.TeleBot(token=cfg.TOKEN)

@bot.message_handler(commands=["start"])
def start_message(message):
    keyboard_markup = types.ReplyKeyboardMarkup()

    tp_shop_button = types.KeyboardButton(text=cfg.TECHNOPARK)
    ca_shop_button = types.KeyboardButton(text=cfg.CREDITASIA)

    keyboard_markup.add(tp_shop_button)
    keyboard_markup.add(ca_shop_button)

    bot.send_message(message.chat.id, cfg.GREETING_MESSAGE, reply_markup=keyboard_markup)

@bot.message_handler(content_types=['text'])
def handle_message(message):
    match message.text:
        case cfg.CREDITASIA:
            message = bot.send_message(message.chat.id, text=cfg.QUERY_MESSAGE, reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, creditasia_handler)

        case cfg.TECHNOPARK:
            message = bot.send_message(message.chat.id, text=cfg.QUERY_MESSAGE, reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, technopark_handler)
        
        case _:
            bot.send_message(message.chat.id, cfg.NOTFOUND_MESSAGE)


def creditasia_handler(message):
    parser = CreditAsiaParser()
    product_list = parser.get_product_list(product_name=message.text)

    for item in product_list:
        bot.send_photo(message.chat.id, photo=item.image, caption=item)

def technopark_handler(message):
    parser = TechnoparkParser()
    product_list = parser.get_product_list(product_name=message.text)

    for item in product_list:
        bot.send_photo(message.chat.id, photo=item.image, caption=item)


if __name__ == '__main__':
    bot.infinity_polling()