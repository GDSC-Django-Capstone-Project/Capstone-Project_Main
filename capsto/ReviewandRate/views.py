from django.shortcuts import render
from .models import Review

def book_reviews(request, book_id):
    reviews = Review.objects.filter(book_id=book_id)
    return render(request, 'book_reviews.html', {'reviews': reviews})
