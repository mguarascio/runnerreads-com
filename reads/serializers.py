from reads.models import Book, Comment
from rest_framework import serializers

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'link')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Book
        fields = ('title', 'link', 'rank', 'comments')

    def create(self, validated_data):
            comments_data = validated_data.pop('comments')
            book, created = Book.objects.get_or_create(link=validated_data['link'])
            print('book: ', book)
            print('created? ', created)
            for comment_data in comments_data:
                Comment.objects.create(book=book, **comment_data)
            return book

