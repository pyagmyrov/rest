from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.models.CharField(max_length=50)
    year = models.models.IntegerField()
    about = models.models.TextField()

    def __str__(self):
        return self.title
    