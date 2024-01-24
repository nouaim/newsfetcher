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
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework import routers
# from newsfetcher.proxy import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api-auth/', include('rest_framework.urls'))
# ]

# from django.urls import path
# from proxy.views import ExternalApiView

# router = routers.DefaultRouter()
# router.register(r'users', views.CategtyViewSet)
# router.register(r'groups', views.CountryViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('external-api/', ExternalApiView.as_view(), name='external-api'),
#     # path('category/', ExternalApiView.as_view(), name='external-api'),
#     # path('country/', ExternalApiView.as_view(), name='external-api'),
#     # path('source/', ExternalApiView.as_view(), name='external-api'),
#     # path('query/', ExternalApiView.as_view(), name='external-api'),
# ]

# urlpatterns += router.urls



from django.urls import path
from proxy.views import TopHeadlinesView, SourcesView

# Develop endpoints for retrieving news (e.g., by category, country, source,query).

urlpatterns = [
    path('top-headlines', TopHeadlinesView.as_view()),
    path('sources', SourcesView.as_view()),
    # ... other endpoints
]