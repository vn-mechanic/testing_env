from random import sample, randint
import telebot
import os

token = os.environ['token']
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def send_welcome(message):

    if message.chat.id != os.environ["chachat"]:
        bot.send_message(os.environ["chachat"], message.text)
        bot.send_message(os.environ["chachat"], message.from_user)

    if "МАРІК" in str(message.text.upper()) or "МАРИК" in str(message.text.upper()) or "MARIK" in str(message.text.upper()):

        if message.from_user.id == 392901615: # ania.me script
            random_number_0 = randint(0, 1)
            if random_number_0 == 0:
                random_number = randint(0, 1)
                if random_number == 0:
                    bot.reply_to(message, "Аню, ви так сьогодні гарно виглядаєте...")
                    bot.send_message(message.chat.id, "...біля дошки")
                elif random_number == 1:
                    bot.send_message(message.chat.id, "@" + str(message.from_user.username) + " хочеш тортика?")
            else:
                random_number = randint(-10, 10)
                random_text = sample(
                    ("Ще одне повідомлення і я тобі поставлю +" + str(random_number),
                     "Підеш наступного понеділка до дошки?", "Дададада", "Кого сьогодні поганяємо?",
                     "Це легко розв\'язується методом честної корупції"), 1)
                bot.reply_to(message, random_text)

        elif message.from_user.id == 382410466: # d15hw45h3r script
            random_number = randint(-10, 10)
            random_text = sample(("Хочеш тортика? виддай 60 грывен)())00)", "Чому тебе сьогодні не було на парі?",
                                  "Лєра го в лс", "Лєра, підеш завтра до дошки?","Дададада", "Кого сьогодні поганяємо?",
                                  "Це легко розв\'язується методом честної корупції",
                                  "Підеш наступного понеділка до дошки?",
                                  "Ще одне повідомлення і я тобі поставлю "+str(random_number),), 1)
            bot.reply_to(message, random_text)

        elif message.from_user.id == 372106864: # Murchik script
            random_number = randint(-10, 10)
            random_text = sample(("Мурчик лох", "Мурчик, ща получиш",
                                  "Тікай з села, ща покличу Пашу", "Мурчик, задача на +6/-20.\n Ти лох?",
                                  "Ще одне повідомлення і я тобі поставлю "+str(random_number),
                                  "Мурчик, купи Лєрі машину", "Мурчик, я піу, а ти кєк", "Щас тебе поганяєм", "Дададада",
                                  "Кого сьогодні поганяємо?","Це легко розв\'язується методом честної корупції",
                                  "Підеш наступного понеділка до дошки?"), 1)
            bot.reply_to(message, random_text)

        elif message.from_user.id == 405633723: # Rymlianyn script
            random_number = randint(-10,10)
            random_text = sample(("Борис, з моїми лабками барісь", "Борис, погнали задачу пвп +5/-1",
                                  "Ще одне повідомлення і я тобі поставлю "+str(random_number),
                                  "Підеш наступного понеділка до дошки?", "Дададада", "Кого сьогодні поганяємо?",
                                  "Це легко розв\'язується методом честної корупції"), 1)
            bot.reply_to(message, random_text)
        else:
            bot.send_message(message.chat.id, sample(("Дададада", "Кого сьогодні поганяємо?","Це легко розв\'язується методом честної корупції"), 1))


        # TODO Add scripts for another users
        # TODO Make good code structure

if __name__ == '__main__':
    bot.polling(none_stop=True)


