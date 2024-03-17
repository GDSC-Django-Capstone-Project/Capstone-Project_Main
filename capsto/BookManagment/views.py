from django.shortcuts import render, redirect, get_object_or_404 
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Book,BorrowedBook
from .forms import BookForm
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.contrib import messages
@login_required
def studentdashboard(request):
    books = Book.objects.all()
    query = request.GET.get('q')
    # If there is a search query, filter books by title containing the query
    if query:
        books = books.filter(title__icontains=query)

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
            return redirect('admindashboard') 
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
            return redirect('admindashboard') 
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        borrowed_books = BorrowedBook.objects.filter(book=book)
        if book.borrowed_books.exists():
            messages.error(request, "This book is borrowed and cannot be deleted.")
            return redirect('admindashboard')
        else:
            book.delete()
            messages.success(request, "deleted successfully!")
            return redirect('admindashboard')
    return render(request, 'delete_book.html', {'book': book})
@login_required    
def borrowed_books(request):
    borrowed_books = BorrowedBook.objects.filter(user = request.user,returned=False)  # Filter only borrowed books
    returned_books = BorrowedBook.objects.filter(returned=True)  # Filter only returned books
    return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books, 'returned_books': returned_books})
"""@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    BorrowedBook.objects.create(book=book, user=request.user)
    messages.success(request, 'Book borrowed successfully!')
    return render(request, 'borrow.html', {'book': book})"""
    
@login_required
def borrow_book(request):
    if request.method == 'POST':
        num_borrowed_books = BorrowedBook.objects.filter(user=request.user).count() 
        if num_borrowed_books >= 3:
            messages.error(request, 'You have already borrowed the maximum number of books allowed.')
            return redirect('studentdashboard')
        else:
            book_id = request.POST.get('book')
            book = get_object_or_404(Book, id=book_id, status='available')
            BorrowedBook.objects.create(book=book, user=request.user)
            messages.success(request, 'Book borrowed successfully!')
            return redirect('studentdashboard')

    
    return render(request, 'borrow.html', {'available_books': Book.objects.filter(status='available')})


"""def logout_view(request):
    logout(request)
    return redirect('home')"""



