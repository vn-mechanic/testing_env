from random import sample
import telebot
import os

token = os.environ['token']
bot = telebot.TeleBot(token)
list_of_participants = []

@bot.message_handler(content_types=["text"])
def send_welcome(message):
    if message.chat.id != 119637031:
        bot.send_message(119637031, message.text)
        bot.send_message(119637031, message.from_user)
    if "МАРІК" in str(message.text.upper()) or "МАРИК" in str(message.text.upper()):
        if message.from_user.username == "mnstrlia" or message.from_user.username == "@d15hw45h3r":
            bot.send_message(message.chat.id, "@mnstrlia, хочеш тортика?")
        else:
            random_text = sample(("Дададада", "Кого сьогодні поганяємо?","Це легко розв\'язується методом честної корупції"), 1)
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


