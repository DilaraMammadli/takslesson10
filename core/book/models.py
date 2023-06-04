from django.db import models


class Book(models.Model):
    name = models.CharField(max_length = 100)
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField()
    update_time = models.DateTimeField()
    

    def __str__(self):
        return self.name