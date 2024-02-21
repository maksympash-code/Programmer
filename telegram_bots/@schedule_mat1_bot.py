import telebot
from telebot import types
bot = telebot.TeleBot("6795598325:AAGTLQKIIdD6DFL6lyMpTNQB2j1RdR3Fk_U")

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Перейти на сайт", url = "https://www.fotor.com/ru/features/one-tap-enhance.html")
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton("Видалити фото", callback_data='delete')
    btn3 = types.InlineKeyboardButton("Змінити текст", callback_data='edit')
    markup.row(btn2,btn3)
    bot.reply_to(message, "Яке красиве фото", reply_markup = markup)


@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.id - 1)
    elif callback.data == "edit":
        bot.edit_message_text('Текст змінено', callback.message.chat.id, callback.message.id)


bot.polling(non_stop=True)