from django.db import models

class Book(models.Model):
    
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    ASIN = models.CharField(max_length=20)
    large_image = models.CharField(max_length=255, null=True)
    medium_image = models.CharField(max_length=255, null=True)
    small_image = models.CharField(max_length=255, null=True)
    tiny_image = models.CharField(max_length=255, null=True)
    rank = models.IntegerField(null=True)

    def __str__(self):
        return self.title + ' : ' + self.ASIN

class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    link = models.CharField(max_length=255)
    score = models.IntegerField(null=True)

    def __str__(self):
        return self.link