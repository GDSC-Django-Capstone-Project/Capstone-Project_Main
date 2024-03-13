from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()

    # Search functionality
    query = request.GET.get('q')
    if query:
        books = books.filter(title__icontains=query)

    # Filter functionality
    genre_filter = request.GET.get('genre')
    if genre_filter:
        books = books.filter(genre=genre_filter)

  

    return render(request, 'book_list.html', {'books': books})
