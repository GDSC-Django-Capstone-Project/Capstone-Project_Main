from django.urls import path
from . import views

urlpatterns = [
    path('books/<int:book_id>/reviews/', views.book_reviews, name='book_reviews'),
    
]
