import telebot
from telebot import types

# from config import TOKEN, exchenges
from config import *
from extensions import Convertor, ApiException

def create_markup(base = None):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    buttons = []
    for val in exchenges.keys():
        if val != base:
          buttons.append(types.KeyboardButton(val.capitalize()))

    markup.add(*buttons)
    return markup


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Приветствие"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for i in exchenges.keys():
        text = '\n'.join((text, i))
    bot.send_message(message.text, text)

@bot.message_handler(commands=['convert'])
def values(message: telebot.types.Message):
    text = 'Выберите валюту, из которой конвертировать: '
    bot.send_message(message.chat.id, text, reply_markup = create_markup())
    bot.register_next_step_handler(message, base_handler)

def base_handler(message: telebot.types.Message):
    base = message.text.strip().lower()
    text = 'Выберите валюту, в которую собираетесь конвертировать: '
    bot.send_message(message.chat.id, text, reply_markup = create_markup(base))
    bot.register_next_step_handler(message, sym_handler, base)

def sym_handler(message: telebot.types.Message, base):
    sym = message.text.strip()
    text = 'Выберите количество конвертирванной валюты: '
    bot.send_message(message.chat.id, text)
    # bot.reply_to(message, text)
    bot.register_next_step_handler(message, amount_handler, base, sym)

def amount_handler(message: telebot.types.Message, base, sym):
    amount = message.text.strip()
    try:
        new_price = Convertor.get_price(base, sym, amount)
    except ApiException as e:
        bot.send_message(message.chat.id, f"Ошибка в конвертации: \n{e} ")
    else:
        text = f"Цена {amount} {base} в {sym} : {new_price}"
        bot.send_message(message.chat.id, text)
    # # bot.register_next_step_handler(message, sym_handler)




bot.polling()
