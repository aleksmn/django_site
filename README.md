# Django Site Example Project

## Usefull commands

Создаем виртуальное окружение
python -m venv .venv 

Активируем виртуальное окружение
.venv\Scripts\activate

Устанавливаем Django
pip install django

Получаем список установленных модулей в данной среде
pip freeze

Создаем новый проект Django
django-admin startproject djangosite .

Создаем новое приложение Django
python manage.py startapp blog

Запускаем сервер разработки
python manage.py runserver

Создаем миграции
python manage.py makemigrations

Применяем миграции
python manage.py migrate

Создаем суперпользователя
python manage.py createsuperuser