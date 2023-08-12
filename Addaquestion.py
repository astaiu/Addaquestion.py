import telebot


bot = telebot.TeleBot("6006599749:AAEak-r6vHAOTfL5SoRvhqZu0uV39zPDua0")

@bot.message_handler(func=lambda message: True)
def add_question_text(message):
    
        new_text = "اضف سوال - " + message.text
        bot.send_message(message.chat.id, new_text)


bot.infinity_polling()