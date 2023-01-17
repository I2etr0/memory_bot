import time

import telebot
from telebot import types
from bot_token import token

TOKEN = token
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
	msg = bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user))
	bot.register_next_step_handler(msg, start_2) # делает линк на вторую функцию, где и происходит изменение сообщения

def start_2(message):
	bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id - 1, text='вы ввели ' + message.text)


bot.polling(none_stop=True)