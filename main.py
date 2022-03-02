import json

import telebot
from telebot import types
import requests
import bs4

bot = telebot.TeleBot('5280932131:AAELkJM_n0-ndTQ-bvmrlCThjDsgcGdYG7A')


@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Главное меню")
    btn2 = types.KeyboardButton("Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я ПайТон. Я могу помочь тебе с выбором книг для чтения.".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "🔙" or ms_text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Жанры")
        btn2 = types.KeyboardButton("Рандом")
        btn3 = types.KeyboardButton("Поиск по названию или автору")
        btn4 = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Жанры":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Детектив")
        btn2 = types.KeyboardButton("Фантастика")
        btn3 = types.KeyboardButton("Приключения")
        btn4 = types.KeyboardButton("Роман")
        btn5 = types.KeyboardButton("Юмор")
        back = types.KeyboardButton("🔙")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(chat_id, text="Открываю жанры", reply_markup=markup)

    elif ms_text == "Детектив":
        bot.send_message(chat_id, text="В стадии разработки")

    elif ms_text == "Фантастика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Фэнтези")
        btn2 = types.KeyboardButton("Научная фантастика")
        back = types.KeyboardButton("🔙")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Перехожу в жанр фантастики", reply_markup=markup)

    elif ms_text == "Фэнтези":
        bot.send_message(chat_id, text="В стадии разработки")

    elif ms_text == "Научная фантастика":
        bot.send_message(chat_id, text="В стадии разработки")

    elif ms_text == "Юмор" or ms_text == "Фольклор" or ms_text == "Роман" or ms_text == "Приключения":
        bot.send_message(chat_id, text="В стадии разработки")

    elif ms_text == "Рандом":
        bot.send_message(chat_id, text=get_book())

    elif ms_text == "Поиск по названию или автору":
        contens = requests.get('https://random.dog/woof.json').json()
        urlDOG = contens['url']
        bot.send_photo(chat_id, photo=urlDOG, caption="Пока работаю над этим. Лови собачку")

    elif ms_text == "Управление":
        bot.send_message(chat_id, text="В стадии разработки")

    elif ms_text == "/help" or ms_text == "Помощь":
        bot.send_message(chat_id, "Автор: Белоцерковец Алина")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напиши автору", url="https://t.me/Litareae")
        key1.add(btn1)
        img = open('Фото.png', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)

    else:

        bot.send_message(chat_id, text="Я тебя слышу! Твое сообщение: " + ms_text)


def get_book():
    array_books = []
    req_book = requests.get('https://readly.ru/books/i_am_lucky/?show=1')
    soup = bs4.BeautifulSoup(req_book.text, "html.parser")
    result_find = soup.select('.blvi__title, .blvi__book_info')
    for result in result_find:
        array_books.append(result.getText().strip())
    return array_books[0] + ' \n' + array_books[1]


bot.polling(none_stop=True, interval=0)

print()
