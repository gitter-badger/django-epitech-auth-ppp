import os
import sys

path = '/var/www/django-epitech-auth-ppp/example/project/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'prod_settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
