# from __future__ import absolute_import, unicode_literals
from celery import Celery
# (Celery task)
app = Celery()
# from celery import shared_task
from proxy.models import NewsItem
import requests
from dotenv import load_dotenv
import os

load_dotenv()
# get the api key as an environment variable
api_key = os.getenv("API_KEY")

# celery configuration
# useful docs concerning schedules: https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#crontab-schedules

@app.task
def add_news_task():
    news_api_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(news_api_url)
    data = response.json()
    for article in data['articles']:
        news = {
            'title': article['title'],
            'content': article['content'],
            'source': article['source']['name'],
            'url': article['url'],
            'published_at': article['publishedAt'],
        }
        # fequently update data according to the time in timedelta in settings
        # use update_or_create() to update data if found
        instance = NewsItem.objects.create(**news)
        instance.save()
