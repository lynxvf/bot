import telebot

bot = telebot.TeleBot("864642148:AAEf2LgdLvfjjKHHodvps1xo5VW0X_f59zI")


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    print(message)


if __name__ == "__main__":
    bot.polling(none_stop=True)