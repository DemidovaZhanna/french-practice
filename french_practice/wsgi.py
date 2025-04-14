"""
Конфигурация WSGI для проекта french_practice.

Этот файл предоставляет переменную уровня модуля с именем ``application``, которая ссылается на WSGI-приложение.
"""

import os

from django.core.wsgi import get_wsgi_application

# Устанавливаем переменную окружения, которая указывает Django, какие настройки использовать
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'french_practice.settings')

# Создаем WSGI-приложение
application = get_wsgi_application()
