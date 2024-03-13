from django.urls import path
from . import views

urlpatterns = [
    #path('books/', views.book_list, name='book_list'),
    path('borrowed/', views.borrowed_books, name='borrowed_books_list'),
    path('borrow/', views.borrow_book, name='borrow_book'),
    path('borrowed/add/', views.add_borrowed_book, name='add_borrowed_book'),
]
