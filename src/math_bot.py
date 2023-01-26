import telebot


bot = telebot.TeleBot("5957069581:AAHnh7Vei0UcvnLGWpiOJ8iADsb9eqShV6Q")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, text="Привет, {0.first_name}, я Математический бот...".format(message.from_user))

@bot.message_handler(commands=["help"])
def send_welcome(message):
	bot.reply_to(message, "Нажмите на интересующую Вас кнопку")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()