"""
Конфигурация WSGI для проекта yatube_api.

Она предоставляет возможность вызова WSGI 
в качестве переменной уровня модуля с именем `application`.

Дополнительную информацию об этом файле смотрите
в разделе https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatube_api.settings')

application = get_wsgi_application()
