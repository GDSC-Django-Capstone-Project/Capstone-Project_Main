from django.apps import AppConfig


class BookmanagmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BookManagment'
class BorrowingConfig(AppConfig):
    name = 'Borrowing'
    verbose_name = 'Borrowing'

    def ready(self):
        
        pass

