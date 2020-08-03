<h2># telegram-shell-bot</h2>

Телеграм-бот (Ubuntu 18.04) позволяющий отправлять команды в терминал ПК и получать результат

**Подготовка программы**
1. После скачивания с гитхаба необходимо создать файл config.yaml
2. Внутри вставить следующее:
        
        #!/usr/bin/python3
        # -*- coding: utf-8 -*-

        ---
        TOKEN : 'токен' # вставить токен своего бота
        TIMEZONE : 'Asia/Almaty'
        TIMEZONE_COMMON_NAME : 'Almaty'

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
1. /start
2. /menu или /commands
3. /help
4. /quit
5. get- команда распознаваемая в терминале

**Демонстрация:**
1. основных возможностей <br>
2. дополнительных возможностей только для владельца телеграм бота

<p>
<img class="aligncenter" src="https://github.com/zhenisduissekov/telegram-shell-bot/blob/master/images/overview.gif" title="Демонстрация основных возможностей" width="370" height="370"/>
&nbsp;&nbsp;&nbsp;
<img class="aligncenter" src="https://github.com/zhenisduissekov/telegram-shell-bot/blob/master/images/extra.gif"  title="Демонстрация дополнительных возможностей только для владельца телеграм бота" width="370" height="370"/>
</p>
