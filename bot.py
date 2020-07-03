import config
import telebot
import string
import time

bot = telebot.TeleBot(config.TOKEN)
GROUP_ID = bot.get_chat("@dptl_reborn").id
restrictedWords = ["test"]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if (message.text.startswith("/") or message.text.startswith("!") or message.text.startswith(".")):
        bot.delete_message(message.chat.id, message.message_id)



    '''swbucks = message.text.startswith("$")
    
    while True:
        if (swbucks == False):
            bot.delete_message(message.chat.id, message.message_id)
            print(message.from_user.username)
        time.sleep(300)'''




bot.polling(none_stop=True, interval=0)
