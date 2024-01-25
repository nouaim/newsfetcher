from django.db import models

class NewsItem(models.Model):
    # title: Text for the news article title.
    title = models.CharField(max_length=255)
    # description: Text for the description.
    description = models.TextField()
    # url: URL to the original news article on the source website.
    url = models.URLField()
    # source: Text for the news source (e.g., "CNN", "BBC").
    source = models.CharField(max_length=255)
    # content: Text for the article's main content.
    content = models.TextField(null=True)
    # published_at: Date and time when the article was published.
    published_at = models.DateTimeField()
    # we can other fields as needed
