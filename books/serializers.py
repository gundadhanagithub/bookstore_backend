from rest_framework import serializers
from books.models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'description', 'author', 'isbn', 'publication_year', 'publisher', 'genre', 'price', 'stock']