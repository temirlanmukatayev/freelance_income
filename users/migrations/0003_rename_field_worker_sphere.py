# Generated by Django 5.0.4 on 2024-04-20 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_worker_customuser_is_client_customuser_is_worker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worker',
            old_name='field',
            new_name='sphere',
        ),
    ]
