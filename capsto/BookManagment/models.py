from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=[('available', 'Available'), ('borrowed', 'Borrowed')], default='available')

    def __str__(self):
        return self.title
