from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Book

def index(request):
    latest_book_list = Book.objects.order_by('rank')[:20]
    context = {'latest_book_list': latest_book_list}
    return render(request, 'reads/index.html', context)

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'reads/detail.html', {'book': book})

class BookDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    """
    Retrieve, update or delete a book instance.
    """
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)