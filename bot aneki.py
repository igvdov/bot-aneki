# -*- coding: utf8 -*-
import telebot

bot = telebot.TeleBot('1745949348:AAEUdJNa4cEs2hN2_4JXh7vp__7Kgg_yf5c')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.message_handler(content_types=['text', 'audio', 'document', 'pictures'])
    if message.text == 'Пельмени' or message.text == 'пельмени':
        bot.send_message(message.from_user.id, "Жена горюет - у мужа что то хуй совсем не стоит... Пошла в аптеку, купила там виагру. \nВрач говорит: \n- По одной ложке в еду!\nЖена думает: да хули одну, надо побольше ебануть, круче будет!\nПришла домой, поставила варить пельмени, сыпанула туда бесконечное количество виагры. И ушла переодеваться. Переоделась, зашла на кухню, а там пельмени мужа ебут")






bot.polling(none_stop=True, interval=0)
