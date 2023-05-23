from django.db import models
from django.utils import timezone


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['-date_posted']
        indexes = [
            models.Index(fields=['-date_posted']),
        ]

    def __str__(self):
        return self.title
