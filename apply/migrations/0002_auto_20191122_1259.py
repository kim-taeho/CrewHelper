# Generated by Django 2.2.7 on 2019-11-22 12:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_on_market'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ApplyProject',
            new_name='Apply',
        ),
    ]
