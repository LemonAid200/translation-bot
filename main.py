import telebot
import get_text
import translator
from os import mkdir
import os.path

if not (os.path.exists('files')):
	mkdir('files')
	if not os.path.exists('files/photos'):
		mkdir('files/photos')

bot = telebot.TeleBot('5925478708:AAHGU-9WmOzjbAKEKHmwUnkJEl79tQ7_bVU')


@bot.message_handler(content_types=['text', 'photo'])

def get_text_messages(message):
	print(message.from_user.username)
	if message.text == "Привет":
		bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
	elif message.text:
		bot.send_message(message.from_user.id, translator.translate(message.text)
)

	elif message.photo:
		handle_docs_photo(message)
	else:
		bot.send_message(message.from_user.id, "Не понимаю такое")


def handle_docs_photo(message):
	file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	src = 'files/' + file_info.file_path
	with open(src, 'wb') as new_file:
			new_file.write(downloaded_file)
	bot.send_message(message.from_user.id, "Обрабатываю")
	text = get_text.extractText(src)
	answer = translator.translate(text)
	bot.reply_to(message, answer)

bot.polling(none_stop=True, interval=0)

