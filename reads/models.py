from django.db import models

class Book(models.Model):
    
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    rank = models.IntegerField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.link