# Generated by Django 5.0.3 on 2024-03-17 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookManagment', '0008_alter_borrowedbook_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookManagment.book'),
        ),
    ]