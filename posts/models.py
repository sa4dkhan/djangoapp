from django.db import models
from datetime import datetime


class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    thumb = models.ImageField(default='default.png', blank=True)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Posts"

