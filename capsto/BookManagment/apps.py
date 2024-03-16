from django.apps import AppConfig


class BookmanagmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BookManagment'
class BorrowingConfig(AppConfig):
    name = 'Borrow'
    verbose_name = 'Borrow'

    def ready(self):
        
        pass

