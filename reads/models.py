from django.db import models

class Book(models.Model):
    
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=2000)
    ASIN = models.CharField(max_length=20)
    large_image = models.CharField(max_length=255, null=True)
    medium_image = models.CharField(max_length=255, null=True)
    small_image = models.CharField(max_length=255, null=True)
    tiny_image = models.CharField(max_length=255, null=True)
    rank = models.IntegerField(null=True)
    product_group = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title + ' : ' + self.ASIN

class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    link = models.CharField(max_length=255)
    score = models.IntegerField(null=True)
    date_time = models.DateTimeField(null=True)
    user = models.CharField(max_length=100, null=True)
    source = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.link