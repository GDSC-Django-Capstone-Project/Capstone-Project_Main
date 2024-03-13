from django.contrib.auth.models import AbstractUser, Permission,Group
from django.db import models

class CustomUser(AbstractUser):
    Student_Role = 'S'
    Admin_Role = 'A'
    SuperAdmin_Role = 'SA'
    ROLE_CHOICES = [
        (Student_Role, 'Student'),
        (Admin_Role, 'Admin'),
        (SuperAdmin_Role,'SuperAdmin')
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES , default = Student_Role )
    class Meta:
        # Define unique related names to resolve clashes with default user model
        permissions = (
            ('view_custom_user', 'Can view custom user'),
        )
        default_related_name = 'custom_users'

    # Add related_name argument to resolve reverse accessor clashes
    groups = models.ManyToManyField(Group, related_name='custom_users_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users_permissions')

