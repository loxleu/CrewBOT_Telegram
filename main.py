import telebot
import random
import re
from telebot import types
# Importing libraries

bot = telebot.TeleBot('1150447891:AAEzlvpteXr3AZWTjsU5I6C--epzvgJgrNs', parse_mode='MarkdownV2')
# Logging in

print('I am ready!')

keyboard = types.InlineKeyboardMarkup()
keyboard.add(types.InlineKeyboardButton(text='Кнопка 1', callback_data='button1'))
keyboard.add(types.InlineKeyboardButton(text='Кнопка 2', callback_data='button2'))
keyboard.add(types.InlineKeyboardButton(text='Открыть сайт', url='https://birdsvoices.github.io/'))


phrases_hello = ["Привет\\!", "Приветик\\!", "Здравствуй, человек\\!", "Приветствую\\!", "О, привет\\!"]
phrases_status = ["Всё нормально\\.", "Всё хорошо\\.", "Всё замечательно\\!"]


@bot.message_handler(commands=['start'])
def start(message):  # Start Command handler
    bot.send_message(message.from_user.id, "Мы стартовали\\! \\(но это не точно\\)")


@bot.message_handler(commands=['info'])
def info(message):  # Info command handler
    bot.send_message(message.from_user.id, "*Тут должна быть всякая разная информация*", reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help_(message):
    bot.send_message(message.from_user.id, "Тут должен был быть список команд")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if re.fullmatch('Привет+', message.text.lower()):
        bot.send_message(message.from_user.id, random.choice(phrases_hello))
    elif re.fullmatch('Как дел(?:а|ишки)\\??+', message.text.lower()):
        bot.send_message(message.from_user.id, random.choice(phrases_status))
    else:
        bot.send_message(message.from_user.id, "Ты говоришь что\\-то непонятное\\. Введи /help, чтобы получить справку по \
                                               командам\\.")


@bot.callback_query_handler(func=lambda call: True)
def handler(call):
    if call.data == 'button1':
        bot.send_message(call.message.chat.id, 'Ты нажал на первую кнопку\\! Поздравляю\\!')
    elif call.data == 'button2':
        bot.send_message(call.message.chat.id, 'Ты нажал на вторую кнопку\\! Поздравляю\\!')


bot.polling(none_stop=True, interval=0)
