# Generated by Django 5.0.2 on 2024-02-21 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trainee',
            new_name='Track',
        ),
    ]