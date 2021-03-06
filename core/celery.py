from __future__ import absolute_import
import os
from celery import Celery
from core.libs.commons.utils import get_default_django_settings_module


# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_default_django_settings_module())


from django.conf import settings  # noqa

app = Celery('coretasks', broker='redis://127.0.0.1:6379/2')


# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))
