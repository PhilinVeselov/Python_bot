import telebot
from telebot import types
import sqlite3


    
#bot
TOKEN ='5727167331:AAEkKA1ZmixB8H_1A2A6enllJtV-o9T_81Y'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('информация о сервисе')
    item2 = types.KeyboardButton('просмотреть услуги')
    item3 = types.KeyboardButton('авторизация / вход')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id,'привет, {0.first_name}! чем могу быть полезен? '.format(message.from_user), reply_markup = markup)
#date base
conn = sqlite3.connect('date_base.db', check_same_thread=False)
cursor = conn.cursor()
def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
	cursor.execute('INSERT INTO users (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
	conn.commit()
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, 'Привет! Ваше имя добавлено в базу данных!')
		
		us_id = message.from_user.id
		us_name = message.from_user.first_name
		us_sname = message.from_user.last_name
		username = message.from_user.username
		
		db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        
bot.polling(none_stop = True)