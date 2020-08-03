#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import os
import datetime
import colorlog


def logger_config(name=None):
    if not name:
        log = logging.getLogger()  # root logger
    else:
        log = logging.getLogger(name)
    log.setLevel(logging.INFO)
    format_str = "%(asctime)s - [%(filename)12s:%(lineno)3s - %(funcName)12s() ]- %(levelname)s - %(message)s"
    date_format = '%d-%b-%y %H-:%M:%S'
    cformat = '%(log_color)s' + format_str
    colors = {'DEBUG': 'green',
              'INFO': 'cyan',
              'WARNING': 'bold_yellow',
              'ERROR': 'bold_red',
              'CRITICAL': 'bold_purple'}
    formatter = colorlog.ColoredFormatter(cformat, date_format, log_colors=colors)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    log.addHandler(stream_handler)
    return log


def logger_config_with_output():
    log_formatter = logging.Formatter(
        "%(asctime)s - [%(filename)12s:%(lineno)3s - %(funcName)12s() ]- %(levelname)s - %(message)s",
        datefmt='%d/%m/%Y %H:%M:%S')
    # Setup File handler
    now = datetime.datetime.now()
    log_file = os.path.join(os.getcwd(), 'output', 'logs', 'output_' + now.strftime("%Y_%m_%d") + '.log')
    file_handler = logging.FileHandler(log_file, "a", "UTF-8")
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)

    # output to console
    app_log = logger_config()

    # output to file
    app_log.addHandler(file_handler)
    return app_log
