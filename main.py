import telebot
from telebot import types

import config as cfg
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
            bot.register_next_step_handler(message, creditasia_handler)

        case cfg.TECHNOPARK:
            bot.register_next_step_handler(message, technopark_handler)
        
        case _:
            bot.send_message(message.chat.id, cfg.NOTFOUND_MESSAGE)

def creditasia_handler(message):
    bot.send_message(message.chat.id, text=cfg.QUERY_MESSAGE)

def technopark_handler(message):
    bot.send_message(message.chat.id, text=cfg.QUERY_MESSAGE)


if __name__ == '__main__':
    bot.infinity_polling()