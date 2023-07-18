import telebot
import webbrowser

bot = telebot.TeleBot('6044281281:AAH0pb6vyjvoMyNznYQRRtEgS01kbc4pcyI')

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, {message.from_user})#.chat.id, "Hello!")


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open("https://stackoverflow.com/")



@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет' or 'hello':
        bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name}')
    elif message.txt.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


# бот не закрывается
bot.polling(none_stop=True)