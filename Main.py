from random import sample
import telebot
from config import token

bot = telebot.TeleBot(token)
list_of_participants = []

@bot.message_handler(content_types=["text"])
def send_welcome(message):
    print(message.text.upper())
    print(message.from_user)
    if "МАРІК" in str(message.text.upper()):
       # with open(r'data.txt', "a+", encoding="utf-8") as data_add:
           # data_add.write((str(message.from_user))+"\n")
        if message.from_user.username == "mnstrlia" or message.from_user.username == "@d15hw45h3r":
            bot.send_message(message.chat.id, "@mnstrlia, хочеш тортика?")
        else:
            random_text = sample(("Дададада", "Кого сьогодні поганяємо?",
                                  "Це легко розв\'язується методом честної корупції"), 1)
            print(random_text)
            print("check")
            bot.send_message(message.chat.id, random_text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
