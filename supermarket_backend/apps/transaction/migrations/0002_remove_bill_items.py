# Generated by Django 5.0.3 on 2024-03-10 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='items',
        ),
    ]
