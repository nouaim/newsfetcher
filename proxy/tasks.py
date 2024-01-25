from __future__ import absolute_import, unicode_literals

# (Celery task)
import celery

@celery.shared_task
def save_news_task(news_objects):
    for news_object in news_objects:
        news_object.save()
    # Logging and any additional processing
