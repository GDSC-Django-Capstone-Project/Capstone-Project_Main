from django.apps import AppConfig

class UserManagementConfig(AppConfig):
    name = 'UserManagment'
    #verbose_name = 'User Management'

    def ready(self):
        # You can perform any initialization tasks here
        pass
