# Generated by Django 5.0.3 on 2024-03-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagment', '0004_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
