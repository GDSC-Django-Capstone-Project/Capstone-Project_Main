from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from UserManagment.models import CustomUser
from django.contrib.auth import get_user_model
#from BookManagment.models import BorrowedBook

class Book(models.Model):
    #book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=[('available', 'Available'), ('borrowed', 'Borrowed')], default='available')
    
    def __str__(self):
        return self.title
    
class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    borrower = models.IntegerField()
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    returned_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)

#  returned = models.BooleanField(default=False)
    def __str__(self):  
        return f"{self.user.username} - {self.book.title}"
    


 



