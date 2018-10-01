from random import sample, randint
import telebot
import os

token = os.environ['token']
bot = telebot.TeleBot(token)
list_of_participants = []


@bot.message_handler(content_types=["text"])
def send_welcome(message):
    #if message.chat.id != 119637031:

        #bot.send_message(119637031, message.text)
        #bot.send_message(119637031, message.from_user)

    if "МАРІК" in str(message.text.upper()) or "МАРИК" in str(message.text.upper()):

        if message.from_user.id == 392901615:
            random_number = randint(0, 1)
            if random_number == 0:
                bot.reply_to(message, "Аню, ви так сьогодні гарно виглядаєте...")
                bot.send_message(message.chat.id, "...біля дошки")
            else:
                bot.send_message(message.chat.id, "@" + str(message.from_user.username) + " хочеш тортика?")

        elif message.from_user.id == 382410466:
            random_text = sample(("Хочеш тортика? виддай 60 грывен)())00)", "Чому тебе сьогодні не було на парі?",
                                  "Лєра го в лс", "Лєра, підеш завтра до дошки?"), 1)
            bot.reply_to(message, random_text)

        else:
            bot.send_message(message.chat.id, sample(("Дададада", "Кого сьогодні поганяємо?","Це легко розв\'язується методом честної корупції"), 1))


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


