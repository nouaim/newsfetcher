# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# import requests
from dotenv import load_dotenv
import os

load_dotenv()

# # get the api key as an environment variable
api_key = os.getenv("API_KEY")

# class ExternalApiView(APIView):
#     def get(self, request, *args, **kwargs):
#         # Specify the API endpoint URL
#         api_url = "https://newsapi.org/v2/top-headlines/sources?apiKey={api_key}"

#         try:
#             # Make a GET request to the API
#             response = requests.get(api_url)

#             if response.status_code == 200:
#                 # Parse the JSON response
#                 data = response.json()
#                 return Response(data, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "Failed to fetch data from the API"}, status=response.status_code)

#         except requests.RequestException as e:
#             # Handle request exceptions (e.g., connection errors)
#             return Response({"error": f"Request error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from rest_framework.views import APIView
from rest_framework.response import Response
# from .models import NewsItem
# from .serializers import NewsItemSerializer
import requests
from .models import NewsItem


class TopHeadlinesView(APIView):
    def get(self, request):
        news_api_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
        response = requests.get(news_api_url)
        data = response.json()

        for article in data['articles']:
            data = {
                'title': article['title'],
                'content': article['content'],
                'source': article['source']['name'],
                'url': article['url'],
                'published_at': article['publishedAt'],
            }
            NewsItem.objects.create(**data)

        # news_items = data['articles']
        # for item in news_items:
        #     # Customize data as needed
        #     item['description'] = item['description'][:150] + '...'

        # serialized_data = NewsItemSerializer(news_items, many=True).data
            
    
        # why it is not working properly
        return Response(data)

class SourcesView(APIView):
    def get(self, request):
        sources = f"https://newsapi.org/v2/top-headlines/sources?apiKey={api_key}"
        response = requests.get(sources)
        data = response.json()
        # news_items = data['articles']
        # for item in news_items:
        #     # Customize data as needed
        #     item['description'] = item['description'][:150] + '...'

        # serialized_data = NewsItemSerializer(news_items, many=True).data
        return Response(data)

# https://newsapi.org/v2/top-headlines/sources?category=businessapiKey=API_KEY
