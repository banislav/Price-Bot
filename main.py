import telebot
from telebot import types

import configuration.config as cfg
from scraping.technopark_parser import TechnoparkParser
from scraping.creditasia_parser import CreditAsiaParser


bot = telebot.TeleBot(token=cfg.TOKEN)

@bot.message_handler(commands=["start"])
def start_message(message, text:str=cfg.GREETING_MESSAGE):
    keyboard_markup = send_keyboard()

    bot.send_message(message.chat.id, text, reply_markup=keyboard_markup)

def send_keyboard():
    keyboard_markup = types.ReplyKeyboardMarkup()

    tp_shop_button = types.KeyboardButton(text=cfg.TECHNOPARK)
    ca_shop_button = types.KeyboardButton(text=cfg.CREDITASIA)

    keyboard_markup.add(tp_shop_button)
    keyboard_markup.add(ca_shop_button)

    return keyboard_markup

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
            start_message(message, text=cfg.UNKNOWNCOMMAND_MESSAGE)


def creditasia_handler(message):
    send_product_list(message, CreditAsiaParser())

    start_message(message, 'Anything else I can do for you?')

def technopark_handler(message):
    send_product_list(message, TechnoparkParser())

    start_message(message, 'Anything else I can do for you?')


def send_product_list(message, parser):
    product_list = parser.get_product_list(product_name=message.text)[:5]
    
    if len(product_list) == 0:
        bot.send_message(message.chat.id, cfg.NOTFOUND_MESSAGE)
    else:
        for item in product_list:
            bot.send_photo(message.chat.id, photo=item.image, caption=item)


if __name__ == '__main__':
    bot.infinity_polling()