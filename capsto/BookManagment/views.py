from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book,BorrowedBook
from .forms import BookForm
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.contrib import messages
@login_required
def studentdashboard(request):
    books = Book.objects.all()
    return render(request, 'studentdashboard.html', {'books': books})
def admindashboard(request):
    books = Book.objects.all()
    return render(request, 'admindashboard.html', {'books': books})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home') 
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'delete_book.html', {'book': book})
@login_required    
def borrowed_books(request):
    borrowed_books = BorrowedBook.objects.filter(user = request.user,returned=False)  # Filter only borrowed books
    returned_books = BorrowedBook.objects.filter(returned=True)  # Filter only returned books
    return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books, 'returned_books': returned_books})
@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    BorrowedBook.objects.create(book=book, user=request.user)
    messages.success(request, 'Book borrowed successfully!')
    return redirect('student_dashboard')

"""@login_required
def borrowed_books(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books})"""

@login_required
def add_borrowed_book(request, book_id):
    book = Book.objects.get(pk=book_id)

    BorrowedBook.objects.create(book=book, user=request.user)
    messages.success(request, 'Book added to borrowed list successfully!')
    return redirect('borrowed_books')

"""def logout_view(request):
    logout(request)
    return redirect('home')"""



