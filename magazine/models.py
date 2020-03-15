from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

