from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BorrowedBook,Book

def borrowed_books(request):
    borrowed_books = BorrowedBook.objects.filter(returned=False)  # Filter only borrowed books
    returned_books = BorrowedBook.objects.filter(returned=True)  # Filter only returned books
    return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books, 'returned_books': returned_books})
@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    BorrowedBook.objects.create(book=book, user=request.user)
    messages.success(request, 'Book borrowed successfully!')
    return redirect('student_dashboard')

@login_required
def borrowed_books(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books})

@login_required
def add_borrowed_book(request, book_id):
    book = Book.objects.get(pk=book_id)

    BorrowedBook.objects.create(book=book, user=request.user)
    messages.success(request, 'Book added to borrowed list successfully!')
    return redirect('borrowed_books')

def logout_view(request):
    logout(request)
    return redirect('home')