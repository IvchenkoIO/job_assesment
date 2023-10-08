import os
from datetime import timedelta

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_test.settings')

app = Celery('job_test')

# Using a string here means the worker doesn't
# have to serialize the configuration object to
# child processes. - namespace='CELERY' means all
# celery-related configuration keys should
# have a `CELERY_` prefix.
app.config_from_object('django.conf:settings',
                       namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
CELERY_BEAT_SCHEDULE = {
    'my_hourly_task': {
        'task': 'task2.celery_tasks.hour_sync',
        'schedule': timedelta(hours=1),
    },
}