# Generated by Django 5.0.3 on 2024-03-17 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookManagment', '0011_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowedbook',
            name='borrower',
        ),
    ]