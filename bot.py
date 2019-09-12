import telebot
import apiai, json

bot = telebot.TeleBot('864642148:AAEf2LgdLvfjjKHHodvps1xo5VW0X_f59zI')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':

        bot.send_message(message.chat.id, 'Ну здравствуй')
        bot.send_sticker(message.chat.id, 'CAADAgADCAADwDZPE29sJgveGptpFgQ')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Ты уверен?')
        bot.send_sticker(message.chat.id, 'CAADAgAD-wADVp29ClYO2zPbysnmFgQ')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgAD9QYAAhPLdwYx70KxXTWCHxYE')



@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()
