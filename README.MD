Обновленный шоблон для бот Aiogram с админкой Django

### Админ панель и модели:
Все модели описываются в файле: admin_panel ➡️ telebot ➡️ models.py.<br>
Функции для доступа к модели в боте описываются в файле: tgbot ➡️ models ➡️ db_commands.py


## Запуск проекта

Склонируйте репозиторий.

Запустить проект можно командой:
 
``` 
docker-compose up
``` 

Утановите разрешенный IP (IP вашего сервера) для админ панели. В папке admin_panel ➡️ admin_panel ➡️ settings.py

```buildoutcfg
ALLOWED_HOSTS = ['<IP вашего сервера>', '127.0.0.1', 'localhost']
```

После команды docker-compose up. Перейдите в контейнер admin_panel

``` 
sudo docker exec -it admin_panel bash
``` 

И пропишите команды:

Для статики:

``` 
python django_app.py collectstatic
``` 

Для сбора миграций:

``` 
python django_app.py makemigrations
``` 

Выполнение миграций:

``` 
python django_app.py migrate
``` 

Создание супер пользователя:

``` 
python django_app.py createsuperuser
``` 
