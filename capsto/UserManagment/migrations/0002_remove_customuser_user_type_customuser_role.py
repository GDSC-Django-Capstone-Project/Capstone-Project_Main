# Generated by Django 5.0.3 on 2024-03-12 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_type',
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('admin', 'Admin'), ('superadmin', 'SuperAdmin')], default={0}, max_length=10),
            preserve_default=False,
        ),
    ]
