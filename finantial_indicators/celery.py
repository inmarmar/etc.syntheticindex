from __future__ import absolute_import
from celery import Celery

"""
celery -A config.celery worker -Q api_queue -n %h-api_queue
"""

app = Celery('template', backend='redis://localhost:6379/0', broker='amqp://guest@localhost://')

app.config_from_object('django.conf:settings', namespace='CELERY')