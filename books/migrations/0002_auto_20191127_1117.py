# Generated by Django 2.2.7 on 2019-11-27 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='descrition',
            new_name='description',
        ),
    ]
