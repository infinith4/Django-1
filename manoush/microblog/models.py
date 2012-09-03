from django.db import models

# Create your models here.

class Note(models.Model):
    author = models.CharField(max_length=30)
    text = models.TextField()
    writed_at = models.DateTimeField()
