from django.db import models

class Book(models.Model):
    
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    ASIN = models.CharField(max_length=20)
    rank = models.IntegerField(null=True)

    def __str__(self):
        return self.title + ' : ' + self.ASIN

class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.link