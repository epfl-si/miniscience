from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniscience.settings')

from django.conf import settings  # noqa

app = Celery('miniscience', broker='amqp://zxtmawyb:i3__oD2W8vyIlNQ8ekUiwFA1dWW4pQ4o@lark.rmq.cloudamqp.com/zxtmawyb')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))