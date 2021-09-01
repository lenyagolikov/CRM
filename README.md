# Базовый функционал CRM на Django
#### Скачивание репозитория, создание и активация виртуального окружения
    git clone https://github.com/lenyagolikov/CRM.git
    cd CRM && python3 -m venv env
    source env/bin/activate
#### Установка нужных зависимостей
    pip install -r requirements.txt
#### Создание базы данных в PostgreSQL: в примере ниже lenyagolikov - имя пользователя, 1234 - пароль, djcrm - название БД
    sudo -u root postgres psql
    create user lenyagolikov with password '1234';
    create database djcrm;
    grant all privileges on database djcrm to lenyagolikov;
#### Создайте файл .env в папке djcrm и скопируйте туда содержимое из .template.env, указав свои значения
    DEBUG=True
    SECRET_KEY='любой секретный ключ в строке'
    DB_NAME=название БД
    DB_USER=имя пользователя БД
    DB_PASSWORD=пароль БД
    DB_HOST=localhost
    DB_PORT=5432
#### Применение миграций, создание суперпользователя и запуск сервера
    python3 manage.py migrate
    python3 manage.py createsuperuser
    python3 manage.py runserver