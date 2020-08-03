# telegram-shell-bot

Телеграм-бот (Ubuntu 18.04) позволяющий отправлять команды в терминал ПК и получать результат

Подготовка программы
1. После скачивания с гитхаба необходимо создать файл config.yaml
2. Внутри вставить следующее:
        
        #!/usr/bin/python3
        # -*- coding: utf-8 -*-

        ---
        TOKEN : 'токен' # вставить токен своего бота
        TIMEZONE : 'Asia/Almaty'
        TIMEZONE_COMMON_NAME : 'Almaty'

        ADMIN: 'username'  # ввести свой пользователь
3. Без этого работать не будет

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
<div class="row">
  <div class="column">
    <img src="https://github.com/zhenisduissekov/telegram-shell-bot/blob/master/images/overview.gif" alt="Overview" width=30>
  </div>
  <div class="column">
    <img src="https://github.com/zhenisduissekov/telegram-shell-bot/blob/master/images/extra.gif" alt="Extra" width=30>
  </div>
</div>


<img src="https://github.com/zhenisduissekov/telegram-shell-bot/blob/master/images/overview.gif?inline=false" width="100" height="100" />
<img src="https://github.com/zhenisduissekov/telegram-shell-bot/blob/master/images/extra.gif?inline=false" width="100" height="100" />


<p data-sourcepos="5:1-7:96" dir="auto">
        <a class="no-attachment-icon" href="https://gitlab.com/dosboxd/question/-/raw/master/with_UUID_crash.gif?inline=false" target="_blank" rel="noopener noreferrer"><img src="https://gitlab.com/dosboxd/question/-/raw/master/with_UUID_crash.gif?inline=false" alt="Alt Text" class="js-lazy-loaded qa-js-lazy-loaded" loading="lazy"></a>
        <a class="no-attachment-icon" href="https://gitlab.com/dosboxd/question/-/raw/master/with_UUID_jumps.gif?inline=false" target="_blank" rel="noopener noreferrer"><img src="https://gitlab.com/dosboxd/question/-/raw/master/with_UUID_jumps.gif?inline=false" alt="Alt Text" class="js-lazy-loaded qa-js-lazy-loaded" loading="lazy"></a>
        </p>
