from django.db import models

class Activity(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.title} - {self.timestamp}"
