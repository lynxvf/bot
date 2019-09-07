import telebot

bot = telebot.TeleBot("864642148:AAEf2LgdLvfjjKHHodvps1xo5VW0X_f59zI")

def start():
    pass


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id,"Пишите слова, бот отвечает на самые интересные из них")


if __name__ == '__main__':
    bot.polling(none_stop=True)