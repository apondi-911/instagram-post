# Generated by Django 4.2.7 on 2023-11-01 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_tag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]