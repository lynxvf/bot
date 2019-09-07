import telebot

bot = telebot.TeleBot("864642148:AAEf2LgdLvfjjKHHodvps1xo5VW0X_f59zI")


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


if __name__ == "__main__":
    bot.polling(none_stop=True)