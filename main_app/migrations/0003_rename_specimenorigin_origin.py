# Generated by Django 4.2.2 on 2023-06-14 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_specimenorigin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SpecimenOrigin',
            new_name='Origin',
        ),
    ]