# pip install pandas
import pandas

# pip install pytelegrambotapi
import telebot  # для работы с telegram ботом

token = 'Убрал'  # токен бота
bot = telebot.TeleBot(token)  # создаем бота

codes = pandas.read_excel('codes.xlsx')  # открываем excel файл с помощью библиотеки pandas

@bot.message_handler(commands=['start'])  # обработчик команды start
def handle_start(message):
    bot.send_message(message.chat.id, 'Отправь код производителя и я пришлю название страны')  # отправляем сообщение

@bot.message_handler(content_types=["text"])  # получение сообщения типа text
def handle_choose(message):
    code = message.text  # берем запрошенный код
    if code[0] == '0':  # если это код от 00 до 09
        # проблема в библиотеке pandas, которая парсит строку 00 в число 0, поэтому страна с таким кодом не найдется.
        # поэтому в таблице у таких чисел в конце приписан символ '
        code = code + "'"  # добавляем служебную черточку
    country = codes.loc[codes['code'] == code]  # ищем в таблице страну с нужным кодом
    result = message.text + ' > ' + country['name']
    if country.size != 0:
        bot.send_message(message.chat.id, result)
    else:
        bot.send_message(message.chat.id, "Страна не найдена")


# запускаем бота
bot.polling(none_stop=True, interval=0)
