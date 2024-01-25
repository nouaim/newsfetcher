from proxy.serializers import NewsSerializer

# from django.views.generic import DetailView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from proxy.models import NewsItem
import requests
from proxy.tasks import save_news_task
from dotenv import load_dotenv
import os
load_dotenv()
# get the api key as an environment variable
api_key = os.getenv("API_KEY")

class TopHeadlinesView(APIView):
    model = NewsItem
    
    def get(self, request):
        news_api_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
        response = requests.get(news_api_url)
        data = response.json()
        ## get the data from the database.
        news_objects = []
        for article in data['articles']:
            news = {
                'title': article['title'],
                'content': article['content'],
                'source': article['source']['name'],
                'url': article['url'],
                'published_at': article['publishedAt'],
            }
            instance = NewsItem.objects.create(**news)
            instance.save()
            # Schedule saving using Celery task
            save_news_task.delay(instance)
        
        # Retrieve inserted data from database
        queryset = NewsItem.objects.all()
        
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)

            

class SourcesView(APIView):
    def get(self, request, category=None, country=None):
        if not category and not country:
            sources = f"https://newsapi.org/v2/top-headlines/sources"
        elif category and not country:
            sources = f"https://newsapi.org/v2/top-headlines/sources?category={category}"
        elif not category and country:
            sources = f"https://newsapi.org/v2/top-headlines/sources?country={country}"
        headers = {'Authorization': api_key}
        try:
            # Make a GET request to the API
            response = requests.get(sources, headers=headers)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Failed to fetch data from the API"}, status=response.status_code)

        except requests.RequestException as e:
            # Handle request exceptions (e.g., connection errors)
            return Response({"error": f"Request error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
