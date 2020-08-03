# telegram-shell-bot

Телеграм-бот (Ubuntu 18.04) позволяющий отправлять команды в терминал ПК и получать результат

Запуск с терминала
1. cd telegram-shell-bot
2. ./start_telegram_shell_bot.sh


Установка в Docker (не обязательна, сделал для пробы)

1. Дать права папке и внутренним папкам

        sudo chown -R zhenis telegram-shell-bot/
        sudo chmod -R 777 telegram-shell-bot/

2. Собрать и запустить докер

       docker build -t telegram-shell-bot .
       docker run --restart=always --name telegram-shell-bot telegram-shell-bot

