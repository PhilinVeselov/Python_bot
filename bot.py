import telebot
from telebot import types
import sqlite3
from requests import get

TOKEN ='5727167331:AAEkKA1ZmixB8H_1A2A6enllJtV-o9T_81Y'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
	
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton('информация о сервисе')
	item2 = types.KeyboardButton('просмотреть услуги')
	markup.add(item1, item2)
	bot.send_message(message.chat.id,'привет, {0.first_name}! чем могу быть полезен? если согласен с использованием чата напиши "привет" '.format(message.from_user), reply_markup = markup )
conn = sqlite3.connect('date_base_telegremm.db', check_same_thread=False)
cursor = conn.cursor()
def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
	cursor.execute('INSERT OR REPLACE INTO infa (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
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
	
	if message.chat.type == 'private':
		#информация о сервисе
		if message.text == 'информация о сервисе':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('немного об авторе данного бота')
			item2 = types.KeyboardButton('описание сервиса')
			back = types.KeyboardButton('другое')
			markup.add(item1, item2, back)
			bot.send_message(message.chat.id,'информация сервиса', reply_markup = markup )
		#немного об авторе данного бота
		if message.text == 'немного об авторе данного бота':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			back = types.KeyboardButton('назад')
			markup.add(back)
			bot.send_message(message.chat.id,'привет дорогой пользователь, я Филин. Я устал всем отвечать в личку на счет цены на мои услуги и решил сделать бота, который облегчит мою жизнь. Я такой же человек, как и все Вы (правда, не играю в игры). ',reply_markup = markup )
		#описание сервиса
		elif message.text == 'описание сервиса':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			back = types.KeyboardButton('назад')
			markup.add(back)
			bot.send_message(message.chat.id,'Данный бот представляеет из себя следущее: здесь ты можешь выбрать для себя нужную услугу. начиная с дополнительного оброзования и заканчивая решением каких-либо задач',reply_markup = markup )
		#назад
		if message.text == 'назад':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('немного об авторе данного бота')
			item2 = types.KeyboardButton('описание сервиса')
			back = types.KeyboardButton('другое')
			markup.add(item1, item2, back)
			bot.send_message(message.chat.id,' ты находишься в блоке "информация о сервисе"',reply_markup = markup )
		#другое
		if message.text == 'другое':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('информация о сервисе')
			item2 = types.KeyboardButton('просмотреть услуги')
			markup.add(item1, item2)
			bot.send_message(message.chat.id,'ты находишься в главном меню',reply_markup = markup )
		
		#просмотреть услуги
		elif message.text == 'просмотреть услуги':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item2 = types.KeyboardButton('полный пакет услуг') #+++++
			item3 = types.KeyboardButton('контрольная точка') #+++++
			item4 = types.KeyboardButton('помощь в реальном времени') #+++++
			item5 = types.KeyboardButton('домашняя работа') #++++
			item6 = types.KeyboardButton('доп. образование') #++++
			item1 = types.KeyboardButton('свзяться с администратором')
			back = types.KeyboardButton('другое')
			markup.add(item2, item3, item4, item5, item6, item1, back)
			bot.send_message(message.chat.id,'здесь ты можешь выбрать нужную для себя услугу, если ничего нет подходящего, то свяжись с администратором',reply_markup = markup )
		
		#полный пакет услуг
		if message.text == 'полный пакет услуг':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('JavaScript')
			item2 = types.KeyboardButton('Английский язык')
			item3 = types.KeyboardButton('Введение в управление проектами')
			item4 = types.KeyboardButton('Дискретная математика')
			item5 = types.KeyboardButton('Информатика (Word, Excel)')
			item6 = types.KeyboardButton('Основы HTML/CSS')
			item7 = types.KeyboardButton('Теория баз данных и основы языка SQL')
			item8 = types.KeyboardButton('Управление веб-серверами')
			item9 = types.KeyboardButton('Элементы высшей математики')
			item21 = types.KeyboardButton('просмотреть услуги')
			markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item21)
			bot.send_message(message.chat.id,'данная услуга включает в себя обсолюно все выше перечеслинные услуги. Пожалуйста выбери нужный для себя предмет',reply_markup = markup )
	
		#контрольная точка
		if message.text == "контрольная точка":
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('JavaScript')
			item2 = types.KeyboardButton('Английский язык')
			item3 = types.KeyboardButton('Введение в управление проектами')
			item4 = types.KeyboardButton('Дискретная математика')
			item5 = types.KeyboardButton('Информатика (Word, Excel)')
			item6 = types.KeyboardButton('Основы HTML/CSS')
			item7 = types.KeyboardButton('Теория баз данных и основы языка SQL')
			item8 = types.KeyboardButton('Управление веб-серверами')
			item9 = types.KeyboardButton('Элементы высшей математики')
			item21 = types.KeyboardButton('просмотреть услуги')
			markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item21)
			bot.send_message(message.chat.id,'данная услуга включает в себя, решение обсолютно всех контрольных точек. Пожалуйста выбери нужный для себя решение  предмет',reply_markup = markup )
		
		#помощь в реальном времени
		if message.text == 'помощь в реальном времени':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('JavaScript')
			item2 = types.KeyboardButton('Английский язык')
			item3 = types.KeyboardButton('Введение в управление проектами')
			item4 = types.KeyboardButton('Дискретная математика')
			item5 = types.KeyboardButton('Информатика (Word, Excel)')
			item6 = types.KeyboardButton('Основы HTML/CSS')
			item7 = types.KeyboardButton('Теория баз данных и основы языка SQL')
			item8 = types.KeyboardButton('Управление веб-серверами')
			item9 = types.KeyboardButton('Элементы высшей математики')
			item21 = types.KeyboardButton('просмотреть услуги')
			markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item21)
			bot.send_message(message.chat.id,'данная услуга включает в себя, обсолютно любую услугу на паре.  Пожалуйста выбери нужный для себя решение  предме.',reply_markup = markup )

		#домашняя работа
		if message.text == 'домашняя работа':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('JavaScript')
			item2 = types.KeyboardButton('Английский язык')
			item3 = types.KeyboardButton('Введение в управление проектами')
			item4 = types.KeyboardButton('Дискретная математика')
			item5 = types.KeyboardButton('Информатика (Word, Excel)')
			item6 = types.KeyboardButton('Основы HTML/CSS')
			item7 = types.KeyboardButton('Теория баз данных и основы языка SQL')
			item8 = types.KeyboardButton('Управление веб-серверами')
			item9 = types.KeyboardButton('Элементы высшей математики')
			item21 = types.KeyboardButton('просмотреть услуги')
			markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item21)
			bot.send_message(message.chat.id,'данная услуга включает в себя, решение домашнего задание.  Пожалуйста выбери нужный для себя решение  предме.',reply_markup = markup )
		
		#доп. образование
		if message.text == 'доп. образование':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('JavaScript')
			item2 = types.KeyboardButton('Английский язык')
			item3 = types.KeyboardButton('Введение в управление проектами')
			item4 = types.KeyboardButton('Дискретная математика')
			item5 = types.KeyboardButton('Информатика (Word, Excel)')
			item6 = types.KeyboardButton('Основы HTML/CSS')
			item7 = types.KeyboardButton('Теория баз данных и основы языка SQL')
			item8 = types.KeyboardButton('Управление веб-серверами')
			item9 = types.KeyboardButton('Элементы высшей математики')
			item21 = types.KeyboardButton('просмотреть услуги')
			markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item21)
			bot.send_message(message.chat.id,'данная услуга включает в себя, дополнительное образование. Если ты немного не понимаешь в предметах, я готов тебе помочь и подтянуть тебя. Пожалуйста выбери нужный для себя решение  предме.',reply_markup = markup )
		
		#пишем код для предметов с выбором подписки
		#JavaScript подписка +
		if message.text == 'JavaScript':
			return bot.send_photo(message.chat.id,open('img/js.png', 'rb'),'Супер, с услугуй уже определились. смотри, цены идут разнае т.к везде разное решение. напиши администратору @philin_bot_sis_admin1 и он тебе с радостью поможет. если ты заказываешь услугу за 1 день до сдачи, то цена вырастит на 30%')
		#Английский язык подписка+
		if message.text == 'Английский язык':
			return bot.send_photo(message.chat.id,open('img/eng.png', 'rb'),'Супер, с услугуй уже определились. смотри, цены идут разнае т.к везде разное решение. напиши администратору @philin_bot_sis_admin1 и он тебе с радостью поможет. если ты заказываешь услугу за 1 день до сдачи, то цена вырастит на 30%')

		#Введение в управление проектами подписка+
		if message.text == 'Введение в управление проектами':
			return bot.send_photo(message.chat.id,'Супер, с услугуй уже определились. смотри, цены идут разнае т.к везде разное решение. напиши администратору @philin_bot_sis_admin1 и он тебе с радостью поможет. если ты заказываешь услугу за 1 день до сдачи, то цена вырастит на 30%')
		#Дискретная математика подписка+
		if message.text == 'Дискретная математика':
			return bot.send_photo(message.chat.id,open('img/mat.png', 'rb'),'Супер, с услугуй уже определились. смотри, цены идут разнае т.к везде разное решение. напиши администратору @philin_bot_sis_admin1 и он тебе с радостью поможет. если ты заказываешь услугу за 1 день до сдачи, то цена вырастит на 30%')
		#Информатика (Word, Excel)
		if message.text == 'Информатика (Word, Excel)':
			return bot.send_photo(message.chat.id,open('img/computer-1884451.png', 'rb'),'Супер, с услугуй уже определились. смотри, цены идут разнае т.к везде разное решение. напиши администратору @philin_bot_sis_admin1 и он тебе с радостью поможет. если ты заказываешь услугу за 1 день до сдачи, то цена вырастит на 30%')
		#Основы HTML/CSS
		if message.text == 'Основы HTML/CSS':
			return bot.send_photo(message.chat.id,open('img/html.png', 'rb'),'Супер, с услугуй уже определились. смотри, цены идут разнае т.к везде разное решение. напиши администратору @philin_bot_sis_admin1 и он тебе с радостью поможет. если ты заказываешь услугу за 1 день до сдачи, то цена вырастит на 30%')
		#Теория баз данных и основы языка SQL
		if message.text == 'Теория баз данных и основы языка SQL':
			return bot.send_photo(message.chat.id,open('img/sql.png', 'rb'),'Супер, с услугуй уже определились. смотри, цены идут разнае т.к везде разное решение. напиши администратору @philin_bot_sis_admin1 и он тебе с радостью поможет. если ты заказываешь услугу за 1 день до сдачи, то цена вырастит на 30%')
		#Управление веб-серверами
		if message.text == 'Управление веб-серверами':
			return bot.send_photo(message.chat.id,open('img/server.png', 'rb'),'Супер, с услугуй уже определились. смотри, цены идут разнае т.к везде разное решение. напиши администратору @philin_bot_sis_admin1 и он тебе с радостью поможет. если ты заказываешь услугу за 1 день до сдачи, то цена вырастит на 30%')
		#Элементы высшей математики +
		if message.text == 'Элементы высшей математики':
			return bot.send_photo(message.chat.id,open('img/mat.png', 'rb'),'Супер, с услугуй уже определились. смотри, цены идут разнае т.к везде разное решение. напиши администратору @philin_bot_sis_admin1 и он тебе с радостью поможет. если ты заказываешь услугу за 1 день до сдачи, то цена вырастит на 30%')
		#свзяться с администратором(нужно дописать код обратной связи) 
		if message.text == 'свзяться с администратором':
			return bot.send_photo(message.chat.id,'Супер, пиши вгруппу и первый освобившийся администратор тебе ответит @philin_bot_sis_admin1 ')


#date base

bot.polling(none_stop=True)
