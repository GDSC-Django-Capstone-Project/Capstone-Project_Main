from django.contrib import admin
from .models import Book,BorrowedBook,Review

admin.site.register(Book)

def mark_as_returned(modeladmin, request, queryset):
    queryset.update(returned=True)

mark_as_returned.short_description = "Mark selected books as returned"

class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'borrowed_date', 'returned_date', 'returned']
    actions = [mark_as_returned]

admin.site.register(BorrowedBook, BorrowedBookAdmin)
admin.site.register(Review)
