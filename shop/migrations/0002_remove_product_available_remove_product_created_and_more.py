# Generated by Django 4.2.7 on 2023-11-21 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated',
        ),
    ]
