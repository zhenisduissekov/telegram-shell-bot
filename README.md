<img class="aligncenter" src="https://img.shields.io/badge/python-3.8-blue.svg"/>
<h2># telegram-shell-bot</h2>

Телеграм-бот (Ubuntu 18.04) позволяющий отправлять команды с телеграмма в терминал ПК и получать результат. На данный момент реализованы следующие запросы вывода: используемой и неиспользуемой памяти, списка  процессов и снимка экрана. Эти три функции реализованы с кнопки. Также вручную можно ввести команды ping или вывода списка файлов и директорий (ls)
Примеры ввода команд вручную:
        <li> get- ping www.google.com -c 1 </li>
        <li> get- ls /home </li>
        <li> get- pwd </li>
        
**Требования к установке**

1. Python 3.8
2. Модули:
<ul>
        <li>certifi==2020.6.20</li>
        <li>chardet==3.0.4</li>
        <li>colorlog==4.2.1</li>
        <li>configparser==5.0.0</li>
        <li>idna==2.10</li>
        <li>Pillow==7.2.0</li>
        <li>pyTelegramBotAPI==3.7.2</li>
        <li>pytz==2020.1</li>
        <li>PyYAML==5.3.1</li>
        <li>requests==2.24.0</li>
        <li>six==1.15.0</li>
        <li>urllib3==1.25.10</li>
        <li>utils==1.0.1</li>
</ul>

**Подготовка программы**
1. После скачивания с гитхаба необходимо создать файл config.yaml
2. Внутри вставить следующее:
        
        #!/usr/bin/python3
        # -*- coding: utf-8 -*-

        ---
        TOKEN : 'токен' # вставить токен своего бота
        ADMIN: 'username'  # ввести свой пользователь

**Запуск с терминала**
1. cd telegram-shell-bot
2. ./start_telegram_shell_bot.sh

**Установка в Docker** (не обязательна, сделал для пробы)
1. Дать права папке и внутренним папкам

        sudo chown -R zhenis telegram-shell-bot/
        sudo chmod -R 777 telegram-shell-bot/

2. Собрать и запустить докер

       docker build -t telegram-shell-bot .
       docker run --restart=always --name telegram-shell-bot telegram-shell-bot

**Использование** 
<ul>
        <li>/start</li>
        <li>/menu или /commands</li>
        <li>/help</li>
        <li>/quit</li>
        <li>get- команда распознаваемая в терминале</li>
</ul>

**Демонстрация:**
1. основных возможностей <br>
2. дополнительных возможностей только для владельца телеграм бота

<p>
<img class="aligncenter" src="https://github.com/zhenisduissekov/telegram-shell-bot/blob/master/images/overview.gif" title="Демонстрация основных возможностей" width="370" height="370"/>
&nbsp;&nbsp;&nbsp;
<img class="aligncenter" src="https://github.com/zhenisduissekov/telegram-shell-bot/blob/master/images/extra.gif"  title="Демонстрация дополнительных возможностей только для владельца телеграм бота" width="370" height="370"/>
</p>
