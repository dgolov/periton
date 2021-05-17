# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1322360/data/www/periton-oil.ru/mysite')
sys.path.insert(1, '/var/www/u1322360/data/env/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
