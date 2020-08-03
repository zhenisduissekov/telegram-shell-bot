#!/usr/bin/python3
# -*- coding: utf-8 -*-

from telebot import types
import sys
from pathlib import Path
import yaml
import os
import time
import datetime
import logging
import text_to_image


def load_config_file():
    if len(sys.argv) < 2:
        file_path = Path('config.yaml')
    else:
        file_path = Path(sys.argv[1])
    if not file_path.exists():
        print('Configuration file does not exist')
        return None
    with file_path.open('r', encoding='utf-8') as stream:
        result_config = yaml.load(stream, Loader=yaml.SafeLoader)
    return result_config


def generate_markup(level):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=False)
    config = load_config_file()
    if level.lower() in ['menu', '/menu']:
        for service in config['menu']:
            markup.add(service['service'])
    return markup


def check_processes():
    result = ''
    for i in os.popen('ps -a'):
        result += i + "\n"
    logging.info(f'Выгрузка данных по памяти из терминала прошла успешно')
    return result


def custom_command(my_command):
    result = ''
    counter = 0
    try:
        for i in os.popen(my_command):
            counter += 1
            result += i + "\n"
            if counter > 30:
                break
        logging.info(f'Выгрузка данных по кастомной команде из терминала прошла успешно')
    except Exception as e:
        logging.error(f'Произошла ошибка при {my_command}')
    return result


def check_memory():
    mem_data = ''
    try:
        for i in os.popen('free'):
            mem_data += i + "\n"
        current_directory = os.path.join(os.popen('pwd').read().strip(), 'output', 'images', 'memory.png')
        result = text_to_image.text2png(mem_data, current_directory)
        logging.info(f'Выгрузка процессов из терминала прошла успешно')
        return result
    except Exception as er:
        logging.error(f'Произошла ошибка при запросе памяти - {er}')
        return None


def take_screenshot():
    try:
        current_directory = os.popen('pwd').read()
        screenshot_directory = os.path.join(current_directory.strip(), 'output', 'screenshots', 'photo.png')
        os.popen(f'gnome-screenshot -f {screenshot_directory}')
        time.sleep(2)
        logging.info(f'Фотографирование экрана прошло успешно')
        return screenshot_directory
    except Exception as er:
        logging.error(f'Произошла ошибка при фотографировании экрана - {er}')
        return None


def insert_unknown_request(unknown_request):
    request_filename = os.path.join('output', 'requests', 'unknown_requests.csv')
    with open(request_filename, 'a', encoding='utf-8') as f:
        f.write(str(datetime.datetime.now()) + ';' + unknown_request + '\n')
    return 0


def check_all_folders():
    if not os.path.exists('output'):
        os.makedirs('output')
    if not os.path.exists(os.path.join('output', 'images')):
        os.makedirs(os.path.join('output', 'images'))
    if not os.path.exists(os.path.join('output', 'logs')):
        os.makedirs(os.path.join('output', 'logs'))
    if not os.path.exists(os.path.join('output', 'requests')):
        os.makedirs(os.path.join('output', 'requests'))
    logging.info('Папки в порядке')
