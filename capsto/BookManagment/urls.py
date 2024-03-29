from django.urls import path
from . import views


urlpatterns = [
    path('booklist/', views.book_list, name='book_list'),
    path('studentdashboard/',views.studentdashboard, name='studentdashboard'),
    path('admindashboard/',views.admindashboard, name='admindashboard'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('addbook/', views.add_book, name='add_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('borrowed_books/', views.borrowed_books, name='borrowed_books'),
    path('borrow/', views.borrow_book, name='borrow'),
    path('create-review/<int:borrowed_book_id>/', views.create_review, name='create_review'),
    path('review-list/', views.review_list, name='review_list'),
    
]
