#!/usr/bin/python3
# -*- coding: utf-8 -*-

from telebot import types
import telebot
import tools
import my_logger
import pytz
import os


config = tools.load_config_file()
bot = telebot.TeleBot(config['TOKEN'])
P_TIMEZONE = pytz.timezone(config['TIMEZONE'])
TIMEZONE_COMMON_NAME = config['TIMEZONE_COMMON_NAME']


@bot.message_handler(commands=['quit'])
def quit_command(message):
    if message.from_user.username == config['ADMIN']:
        bot.send_message(message.chat.id, 'Программа остановлена')
        bot.stop_polling()
        logging.warning('Программа закончена по вызову')
    else:
        bot.send_message(message.chat.id, 'Извините, но вы не имеете доступа к данной функции')
        logging.error(f'{message.from_user.first_name} '
                      f'{message.from_user.last_name} '
                      f'({message.from_user.username}) пытался остановить программу')


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Приветствую!\n' +
        'Для просмотра функционала бота напишите или выберете ***/commands*** или ***/menu***\n' +
        'Описание программы ***/help***',
        parse_mode='Markdown'
    )


@bot.message_handler(commands=['help', 'info'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url='telegram.me/zduissekov'
        )
    )
    bot.send_message(
        message.chat.id,
        "Я написал этот бот в целях саморазвития.\n"
        "С его помощью я могу контролировать мой домашний ПК\n\n" 
        "Он легко покажет мне: \n"
        "           запущенные процессы,\n"
        "           занятость памяти,\n"
        "           что открыто на экране,\n\n"
        "Если заметите ошибку или есть предложения пишите мне в личку\n\n"
        "Спасибо",
        parse_mode='Markdown',
        reply_markup=keyboard
    )


@bot.message_handler(commands=['commands', 'menu', 'quit'])
def menu_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Git', url='https://zhenisduissekov.github.io'))
    keyboard.add(telebot.types.InlineKeyboardButton('Memory', callback_data="Memory"))
    keyboard.add(telebot.types.InlineKeyboardButton('Processes', callback_data='Processes'))
    keyboard.add(telebot.types.InlineKeyboardButton('Screenshot', callback_data="Screenshot"))
    bot.send_message(message.chat.id, 'Что вас интересует?', reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        logging.info(f'Принята команда {call.data}')
        if call.message:
            if call.data == "Memory":
                logging.info('Запрос на просмотр памяти')
                image = tools.check_memory()
                bot.send_photo(message.chat.id, (os.path.basename(image), open(image.strip(), "rb")))
            if call.data == "Processes":
                logging.info('Запрос на просмотр процессов')
                result = tools.check_processes()
                bot.send_message(message.chat.id, result)
            if call.data == "Screenshot":
                logging.info('Запрос на просмотр экрана')
                image = tools.take_screenshot()
                if image is not None:
                    bot.send_message(message.chat.id, 'Скриншот')
                    bot.send_photo(message.chat.id, (os.path.basename(image), open(image.strip(), "rb")))
                else:
                    bot.send_message(message.chat.id, 'Фото не сохранилось')


@bot.message_handler(content_types=['text'])
def unexpected_messages(message):
    logging.warning(f'Получено сообщение "{message.text}"')
    if message.text.startswith('get-') and message.from_user.username == config['ADMIN']:
        custom_command = message.text.strip('get-')
        result = tools.custom_command(custom_command)
        bot.send_message(message.chat.id, result)
        return 0
    else:
        reply_msg = 'Извините, я вас не понимаю, но ваш вопрос будет занесен в базу для последующего просмотра'
        bot.send_message(message.chat.id, reply_msg, parse_mode="Markdown")
        tools.insert_unknown_request(message.text)
        logging.info(f'Выдан ответ - "{reply_msg}"')
        return 0


if __name__ == '__main__':
    tools.check_all_folders()
    logging = my_logger.logger_config_with_output()
    logging.info('Телеграм бот запущен')
    bot.polling(none_stop=True)
