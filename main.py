import typing
from requests import get
import telebot
from telebot import types
import configuration.config as cfg
from item import Item
from scraping.technopark_parser import TechnoparkParser
from scraping.creditasia_parser import CreditAsiaParser


bot = telebot.TeleBot(token=cfg.TOKEN)

@bot.message_handler(commands=["start"])
def start_message(message, text:str=cfg.GREETING_MESSAGE) -> None:
    keyboard_markup = send_keyboard()

    bot.send_message(message.chat.id, text, reply_markup=keyboard_markup)
    bot.register_next_step_handler(message, handle_message)

def send_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard_markup = types.ReplyKeyboardMarkup()

    tp_shop_button = types.KeyboardButton(text=cfg.TECHNOPARK)
    ca_shop_button = types.KeyboardButton(text=cfg.CREDITASIA)
    compare_button = types.KeyboardButton(text=cfg.COMPARE)

    keyboard_markup.add(tp_shop_button)
    keyboard_markup.add(ca_shop_button)
    keyboard_markup.add(compare_button)

    return keyboard_markup


def handle_message(message) -> None:
    match message.text:
        case cfg.CREDITASIA:
            message = bot.send_message(message.chat.id, text=cfg.QUERY_MESSAGE, reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, creditasia_handler)

        case cfg.TECHNOPARK:
            message = bot.send_message(message.chat.id, text=cfg.QUERY_MESSAGE, reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, technopark_handler)

        case cfg.COMPARE:
            message = bot.send_message(message.chat.id, text=cfg.QUERY_MESSAGE, reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, compare_handler)
        
        case _:
            start_message(message, text=cfg.UNKNOWNCOMMAND_MESSAGE)


def compare_handler(message) -> None:
    ca_result = send_product_list(message, CreditAsiaParser(), product_number=1)[0]
    tp_result = send_product_list(message, TechnoparkParser(), product_number=1)[0]

    msg = f"{ca_result.source}: {ca_result.name} {ca_result.price}\n" + f"{tp_result.source}: {tp_result.name} {tp_result.price}"
    bot.send_message(message.chat.id, text=msg)

    start_message(message, cfg.ASKAGAIN_MESSAGE)


def creditasia_handler(message) -> None:
    send_product_list(message, CreditAsiaParser(), product_number=5)

    start_message(message, cfg.ASKAGAIN_MESSAGE)

def technopark_handler(message) -> None:
    send_product_list(message, TechnoparkParser(), product_number=5)

    start_message(message, cfg.ASKAGAIN_MESSAGE)


def send_product_list(message, parser, product_number:int) -> typing.List[Item]:
    product_list = parser.get_product_list(product_name=message.text)[:product_number]
    
    if len(product_list) == 0:
        bot.send_message(message.chat.id, cfg.NOTFOUND_MESSAGE)
    else:
        for item in product_list:
            img = get(item.image)
            bot.send_photo(message.chat.id, photo=img.content, caption=item)
    
    return product_list


if __name__ == '__main__':
    bot.infinity_polling()