# Generated by Django 5.1 on 2024-09-27 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]
