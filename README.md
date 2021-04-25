# SMTP client

Отправляет картинки из указанной директории на email

## Установка

    git clone https://github.com/OxyEho/SMTP-client.git

## Запуск 

    python -m client --from example@mail.ru --to example@mail.ru --ssl --auth 
        --verbose --subject Theme --server smtp.mail.ru:25 --directory some_directoty
    
    --from указывает с какого адреса отправлять письмо
    
    --to указывает на какой адрес отправлять письмо

    --ssl устанавливает защищенное соедениение

    --auth запрашивает авторизация отправителя

    --verbose отображет входящие и исходящие сообщения

    --subject указывает тему письма

    --server указывает к какому серверу и по какому порту подключиться

    --directory директория откуда будут взяты картинки