from __future__ import absolute_import, unicode_literals
from django.conf import settings
import os
import django
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'bestdeals.settings')
django.setup()

app = Celery('bestdeals', backend='redis://localhost:6379/0',
             broker='amqp://guest@localhost//')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
