# telegram-shell-bot

Телеграм-бот позволяющий отправлять команды в терминал ПК и получать результат



Установка в Docker
Дать права папке и внутренним папкам
sudo chown -R zhenis telegram-shell-bot/
sudo chmod -R 777 telegram-shell-bot/

Собрать и запустить докер
docker build -t telegram-shell-bot .
docker run --restart=always --name telegram-shell-bot telegram-shell-bot