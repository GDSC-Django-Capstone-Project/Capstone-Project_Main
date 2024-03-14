from django.contrib.auth.models import AbstractBaseUser,  PermissionsMixin,Group,Permission
from django.db import models
from django.utils import timezone
from .manager import CustomUserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):
    Student_Role = 'S'
    Admin_Role = 'A'
    SuperAdmin_Role = 'SA'
    ROLE_CHOICES = [
        (Student_Role, 'Student'),
        (Admin_Role, 'Admin'),
        (SuperAdmin_Role,'SuperAdmin')
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES , default = Student_Role )
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length = 255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    USERNAME_FIELD = 'username'
    
    objects = CustomUserManager()
    
    class Meta:
        # Define unique related names to resolve clashes with default user model
        permissions = (
            ('view_custom_user', 'Can view custom user'),
        )
        default_related_name = 'custom_users'

    # Add related_name argument to resolve reverse accessor clashes
    groups = models.ManyToManyField(Group, related_name='custom_users_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users_permissions')

