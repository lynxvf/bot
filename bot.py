import telebot
import apiai, json

bot = telebot.TeleBot('864642148:AAEf2LgdLvfjjKHHodvps1xo5VW0X_f59zI')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text.lower() == 'привет':
#
#         bot.send_message(message.chat.id, 'Ну здравствуй')
#         bot.send_sticker(message.chat.id, 'CAADAgADCAADwDZPE29sJgveGptpFgQ')
#     elif message.text.lower() == 'пока':
#         bot.send_message(message.chat.id, 'Ты уверен?')
#         bot.send_sticker(message.chat.id, 'CAADAgAD-wADVp29ClYO2zPbysnmFgQ')
#     elif message.text.lower() == 'я тебя люблю':
#         bot.send_sticker(message.chat.id, 'CAADAgAD9QYAAhPLdwYx70KxXTWCHxYE')


@bot.message_handler(content_types=['text'])
def text_message(update):
    request = apiai.ApiAI('864642148:AAEf2LgdLvfjjKHHodvps1xo5VW0X_f59zI').text_request()
    request.lang = 'ru'
    request.session_id = 'lolstickerbot'
    request.query = update.text
    response_json = json.loads(request.getresponse().read().decode('utf-8'))
    response = response_json['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=update.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.mchat_id, text='Я Вас не совсем понял!')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()
