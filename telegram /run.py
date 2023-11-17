import config
import telebot
from telebot import types
import pandas_functions


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def get_start(message):
    keyboard = types.ReplyKeyboardMarkup()
    buttonA = types.KeyboardButton("find artist")
    buttonB = types.KeyboardButton("get playlist by year")
    keyboard.add(buttonA, buttonB)
    bot.send_message(message.chat.id, f"We have a dataset with size of {pandas_functions.get_shape()}", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def buttonA_func(message):
    if message.text == 'find artist':
        bot.send_message(message.chat.id, "What artist?")
    else:
        reply = pandas_functions.get_artist_by_name((message.text))
        bot.send_message(message.chat.id, reply, parse_mode="Markdown")


if __name__ == "__main__":
    bot.infinity_polling()

