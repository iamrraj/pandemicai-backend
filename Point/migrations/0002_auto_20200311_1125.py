# Generated by Django 2.2 on 2020-03-11 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Point', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminuser',
            old_name='locaton',
            new_name='location',
        ),
    ]