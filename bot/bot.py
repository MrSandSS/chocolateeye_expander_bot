import random
import telebot

bot = telebot.TeleBot("")

diameter = 0  # Глобальный диаметр

# обработка /start
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == "private":  # Только для личных чатов
        bot.send_message(message.chat.id, 'Разработано @mrsand_ss')
        bot.send_message(message.chat.id, "👋 Привет! "
                                           "Я – специалист по шоколадному глазу. "
                                           "Разбираюсь в нём лучше, чем любой спелеолог.")
        bot.send_message(message.chat.id, '• Введите "/expand", чтобы расширить шоколадный глаз'
                                           '\n• Введите "/status", чтобы узнать текущий диаметр '
                                           'шоколадного глаза')
    else:
        bot.send_message(message.chat.id, "Я работаю и в группах! Введите /expand или /status.")


# обработка /expand
@bot.message_handler(commands=['expand'])
def expand(message):
    global diameter
    attempt = int(random.triangular(0, 20, 4))  # Генерация случайного расширения
    diameter += attempt

    if attempt == 0:
        bot.send_message(message.chat.id, f'😰 К сожалению, шоколадный глаз не расширен. '
                                          f'Попробуйте ещё раз.\nСейчас диаметр: {diameter} см.')
    elif attempt == 20:
        bot.send_message(message.chat.id, f'🎉 МАКСИМАЛЬНОЕ РАСШИРЕНИЕ! +{attempt} см 👨🏿‍🦳 '
                                          f'\nСейчас диаметр: {diameter} см.')
    else:
        bot.send_message(message.chat.id, f'🔥 Поздравляю! Твой шоколадный глаз расширен на {attempt} см!'
                                          f'\nСейчас диаметр: {diameter} см.')

    bot.send_message(message.chat.id, 'Введите "/expand", чтобы продолжить!')


# обработка /status
@bot.message_handler(commands=['status'])
def status(message):
    radius = diameter / 2
    area = (radius ** 2) * 3.1415926535  # πr^2

    bot.send_message(message.chat.id, f'📏 Диаметр: {diameter} см.\n'
                                      f'🔘 Радиус: {radius:.2f} см.\n'
                                      f'🟤 Площадь: {area:.2f} см².')


# Запуск бота
bot.polling(none_stop=True, interval=0)
