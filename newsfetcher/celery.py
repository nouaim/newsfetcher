import os

from celery import Celery
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsfetcher.settings')

app = Celery('newsfetcher')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='NEWSFETCHER')

app.conf.beat_schedule = {
    'addnews': {
        'task': 'proxy.tasks.add_news_task',
        'schedule': crontab(minute='*/15'),# Execute every 15 minutes.
    },
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()



@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')