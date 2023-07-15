import telebot

bot = telebot.TeleBot('6044281281:AAH0pb6vyjvoMyNznYQRRtEgS01kbc4pcyI')

@bot.message_handler(commands=['start'])

def main(message):
    bot.send_message(message.chat.id, "Hello!")

# бот не закрывается
bot.polling(none_stop=True)