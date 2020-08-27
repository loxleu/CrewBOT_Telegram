import telebot

bot = telebot.TeleBot('1150447891:AAEzlvpteXr3AZWTjsU5I6C--epzvgJgrNs')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Мы стартовали! (но это не точно)")


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.from_user.id, "*Тут должна быть всякая разная информация*")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, "О, привет!")
    elif message.text == '/help':
        bot.send_message(message.from_user.id, "Тут должен был быть список команд")
    else:
        bot.send_message(message.from_user.id, "Ты говоришь что-то непонятное.")


bot.polling(none_stop=True, interval=0)
