# telegram-shell-bot

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
3. Без этого работать не будет

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

**Демонстрация:**
1. основных возможностей <br>
2. дополнительных возможностей только для владельца телеграм бота

<p><figure><figcaption>основных возможностей</figcaption>
<img class="aligncenter" src="https://github.com/zhenisduissekov/telegram-shell-bot/blob/master/images/overview.gif" width="300" height="300" 
/>
&nbsp;&nbsp;&nbsp;
<figcaption>дополнительных возможностей только для владельца телеграм бота</figcaption>
<img class="aligncenter" src="https://github.com/zhenisduissekov/telegram-shell-bot/blob/master/images/extra.gif"  width="300" height="300" />
</figure>
</p>

<p>
<div id="images" class="row">
    <div class="column">
        <img src="https://github.com/zhenisduissekov/telegram-shell-bot/blob/master/images/extra.gif" width="100px" height="100px">
        <div class="caption">Caption 1</div>
    </div>
    <div class="column">
        <img src="https://github.com/zhenisduissekov/telegram-shell-bot/blob/master/images/extra.gif" width="100px" height="100px"> 
        <div class="caption">Caption 2</div>
    </div>
</div>
</p>

/* Three image containers (use 25% for four, and 50% for two, etc) */
.column {
  float: left;
  width: 33.33%;
  padding: 5px;
}

/* Clear floats after image containers */
.row::after {
  content: "";
  clear: both;
  display: table;
}

<div class="row">
  <div class="column">
    <img src="img_snow.jpg" alt="Snow" style="width:100%">
  </div>
  <div class="column">
    <img src="img_forest.jpg" alt="Forest" style="width:100%">
  </div>
  <div class="column">
    <img src="img_mountains.jpg" alt="Mountains" style="width:100%">
  </div>
</div>

