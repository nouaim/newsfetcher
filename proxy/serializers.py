from rest_framework import serializers
from .models import NewsItem

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = '__all__'