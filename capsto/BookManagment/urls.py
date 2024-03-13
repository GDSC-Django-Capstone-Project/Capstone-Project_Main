from django.urls import path
from . import views


urlpatterns = [
    path('booklist/', views.book_list, name='book_list'),
    path('studentdashboard/',views.student_dashboard, name='student_dashboard'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('addbook/', views.add_book, name='add_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('borrowed/', views.borrowed_books, name='borrowed_book'),
    path('borrow/', views.borrow_book, name='borrow_book'),
    path('borrowed/add/', views.add_borrowed_book, name='add_borrowed_book'),
    
]
