# VPS API

Данный проект реализует тестовое задание от компании JustHost.
Проект представляет собой REST-сервис для управления виртуальными серверами (VPS) с поддержкой следующего функционала:
- Создание нового виртуального сервера
- Получение данных о конкретном сервере по его uid.
- Вывод списка всех серверов с поддержкой фильтрации по заданным параметрам.
- Изменение статуса сервера (например, перевод в состояния started, blocked, stopped).

## Запуск проекта:

### 1. Клонируйте репозиторий:
`git clone https://github.com/Banan4k2002/api_vps_managing.git`

### 2. Cоздайте и активируйте виртуальное окружение:
Windows:
- `python -m venv venv`
- `source venv/Scripts/activate`

Linux/Mac:
- `python3 -m venv venv`
- `source venv/bin/activate`

### 3. Обновите пакетный менеджер и установите зависимости:
- `pip install --upgrade pip`
- `pip install -r requirements.txt`

### 4. Перейдите в директорию проекта:
`cd app/`

### 5. Примените миграции:
`python manage.py migrate`

### 6. Создайте суперпользователя для доступа к админ-зоне:
`python manage.py createsuperuser`

### 7. Запустите сервер разработки:
`python manage.py runserver`

## Документация API
Документация API доступна по адресу `http://127.0.0.1:8000/` после запуска проекта.

## Использованные технологии:
- Python 3.10.15
- Django 5.1.4
- Django REST Framework 3.15.2
- Drf-yasg 1.21.8
