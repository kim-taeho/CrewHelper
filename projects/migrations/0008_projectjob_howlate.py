# Generated by Django 2.2.7 on 2019-12-12 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_projectjob_isfinished'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectjob',
            name='howLate',
            field=models.DateField(null=True),
        ),
    ]
