"""models
"""
from django.db import models


class Book(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=100)
    description = models.CharField(verbose_name="説明", max_length=100)

    class Meta:
        db_table = 'books'
