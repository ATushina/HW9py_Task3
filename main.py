#Создать телефонный справочник 
# с возможностью импорта и экспорта данных 
# в нескольких форматах.

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from spy import*

TOKEN = "5854704525:AAEOF22PPomZ6eggfdY2ee9YePhUTptVfNo"
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['tel_book.csv'])
def start_db(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    search_contact = types.KeyboardButton('Найти контакт')
    add_contact = types.KeyboardButton('Добавить контакт')
    markup.add(search_contact, add_contact)
    bot.send_message(message.chat.id, 'Добро пожаловать', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    file = file.open_file('tel_book.csv')
    if message.text == 'Найти контакт':
        bot.send_message(message.chat.id, 'Можно искать по фамилии и номеру телефона....')
    elif message.text == 'Добавить запись':
        bot.send_message(message.chat.id, 'Введите данные для добавления....')
        bot.register_next_step_handler(message, add_contact)


def search_contact():
    search_str = input('Введите запрос (можно искать по фамилии и номеру телефона): ...')
    data = open_file('tel_book.txt').split('\n')
    header = data[0]
    data = data[1:len(data) - 1]
    res = list(filter(lambda el: el.find(search_str) != -1, data))
    if len(res) == 0:
        print('Нет такого контакта')
    else:
        res.insert(0, header)
        print('\n'.join(res))


def add_contact():
    new_contact = input('Введите данные контакта (формат "ФИО телефон"): ')
    new_contact += '\n'
    write_to_file(new_contact, 'tel_book.csv')
    write_to_file(new_contact, 'tel_book.txt')

def open_file(file_name):
    with open(file_name, 'r') as data:
        file_content = data.read()
    return file_content

def write_to_file(text: str, file_name: str):
    with open(file_name, 'a') as data:
        data.write(text)

app = ApplicationBuilder().token("5854704525:AAEOF22PPomZ6eggfdY2ee9YePhUTptVfNo").build()

app.add_handler(CommandHandler("Найти контакт", search_contact))
app.add_handler(CommandHandler("Добавить контакт", add_contact))

app.run_polling()

from controller import run_prog
run_prog()
