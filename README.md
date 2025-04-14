# Тренажер для изучения Французского языка
Отчетный проект по теме "Разработка web-приложения на Django"

## Как использовать

1. Клонировать репозиторий
2. В директории репозитория выполнить следующие команды:  
`pip install -r requirements.txt`  
`python manage.py runserver --insecure`

## Версии ПО

Предполагается использование версии 4.1.7 фреймворка Django.

# Проект french-practice
Проект представляет собой web-сервис на Django, темой которого является тренажер для изучения французского языка. Данный сервис предоставляет возможность изучения информации, необходимой для выполнения различных практических заданий, включая *перевод текстов*, содержащих слова из *словаря* и выполнения *мини-викторины*. В приложении реализованы формы для ввода ответов, а также отображение результатов в виде оценок.

## Установка и настройка

1. **Клонирование репозитория:**

    ```bash
    git clone git@github.com:DemidovaZhanna/french-practice.git
    cd french-practice
    ```

2. **Создание виртуального окружения:**

    На Windows:
    ```bash
    python -m venv venv
    ```

    На MacOS/Linux:
    ```bash
    python3 -m venv venv
    ```

3. **Активация виртуального окружения:**

    На Windows:
    ```bash
    venv\Scripts\activate
    ```

    На MacOS/Linux:
    ```bash
    source venv/bin/activate
    ```

4. **Установка зависимостей:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Создание файла `.env` в корне проекта и добавление в него необходимых переменные окружения, например:**

    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```

6. **Применение миграций:**

    ```bash
    python manage.py migrate
    ```

7. **Запуск сервера:**

    ```bash
    python manage.py runserver
    ```

8. Web-сервис располагается по адресу `http://127.0.0.1:8000/`.

## Структура проекта

- `french_practice/` — основной каталог проекта.
    - `settings.py` — файл настроек Django.
    - `urls.py` — файл маршрутизации URL.
    - `wsgi.py` — настройка для WSGI.
    - `asgi.py` — настройка для ASGI.
- `templates/` — каталог с HTML-шаблонами.
- `static/` — каталог с статическими файлами (CSS, JavaScript, изображения).
- `staticfiles/` — директория для собранных статических файлов.
- `.env` — файл с переменными окружения (секретный ключ, настройки).

## Технологии

- Python 3.12+
- Django 4.1.7

## Ссылки

- [Документация Django](https://docs.djangoproject.com/en/4.1/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)