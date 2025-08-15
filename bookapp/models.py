from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='Unknown Author')
    description = models.TextField(default='No description available')
    rating = models.FloatField(default=0.0)  # Set default to 0.0 (float)
    cover_url = models.URLField(default='https://example.com/default-cover.jpg')

class UserBookStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('TBR', 'TBR'), ('Reading', 'Reading'), ('Completed', 'Completed')])

    class Meta:
        unique_together = ('user', 'book')

