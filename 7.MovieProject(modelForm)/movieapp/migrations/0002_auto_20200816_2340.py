# Generated by Django 3.0.7 on 2020-08-16 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='rdate',
            new_name='Release Date',
        ),
    ]