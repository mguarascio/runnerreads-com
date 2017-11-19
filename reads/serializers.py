from reads.models import Book, Comment
from rest_framework import serializers
from reads.amazon import Amazon

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'link', 'score')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Book
        fields = ('title', 'link', 'ASIN', 'rank', 'comments')

    def create(self, validated_data):
        comments_data = validated_data.pop('comments')
        book = None
        try:
            book = Book.objects.get(ASIN=validated_data['ASIN'])
        except:
            print('book ASIN not found: ', validated_data['ASIN'])
            # not found
        
        if not book:
            amazon = Amazon()
            product = amazon.lookup(validated_data['ASIN'])
            if product:
                book = Book(ASIN=validated_data['ASIN'], link=product.detail_page_url, title=product.title, large_image=product.large_image_url, medium_image=product.medium_image_url, small_image=product.small_image_url, tiny_image=product.tiny_image_url, rank=9999)
                book.save()
                
        if book:
            print('book: ', book)
            for comment_data in comments_data:
                Comment.objects.create(book=book, **comment_data)

        return book