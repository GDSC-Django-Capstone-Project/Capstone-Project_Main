from django.apps import AppConfig

class ReviewAndRatingConfig(AppConfig):
    name = 'ReviewandRate'
    verbose_name = 'Review and Rating'

    def ready(self):
        # You can perform any initialization tasks here
        pass
