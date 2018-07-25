from random import sample
import telebot
#import os
#from flask import Flask, request


#server = Flask(__name__)

token = '668673628:AAHmhNZDN9qdO2-Aqb4ogPV-tbJd2flbN7s'
token2 = "562189430:AAG9Gx26wRCvH8Jeb-mB11tEkWu2FjaLitU"
bot = telebot.TeleBot(token2)
list_of_participants = []

@bot.message_handler(content_types=["text"])
def send_welcome(message):
    #print(message.text.upper())
    #print(message.from_user)
    if "МАРІК" in str(message.text.upper()):
       # with open(r'data.txt', "a+", encoding="utf-8") as data_add:
           # data_add.write((str(message.from_user))+"\n")
        if message.from_user.username == "mnstrlia" or message.from_user.username == "@d15hw45h3r":
            bot.send_message(message.chat.id, "@mnstrlia, хочеш тортика?")
        else:
            random_text = sample(("Дададада", "Кого сьогодні поганяємо?",
                                  "Це легко розв\'язується методом честної корупції"), 1)
            #print(random_text)
            #print("check")
            bot.send_message(message.chat.id, random_text)

'''@server.route("/"+token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://t.me/marik_bot")
    return "!", 200

server.run(host="127.0.0.1", port=os.environ.get('PORT', 5000))'''

if __name__ == '__main__':
    bot.polling(none_stop=True)

