"""
URL configuration for newsfetcher project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from proxy.views import TopHeadlinesView, SourcesView

# Develop endpoints for retrieving news (e.g., by category, source, country...).

urlpatterns = [
    path('top-headlines/', TopHeadlinesView.as_view()),
    path('sources&category=<str:category>/', SourcesView.as_view()), ## example for buiness:  http://127.0.0.1:8000/sources&category%3Dbusiness/
    path('sources&country=<str:country>/', SourcesView.as_view()), ## example for Saudi Arabia: http://127.0.0.1:8000/sources&country%3Dsa/
    path('sources/', SourcesView.as_view()),
    # ... other endpoints
]
