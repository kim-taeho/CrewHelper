# Generated by Django 2.2.7 on 2019-12-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20191218_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectjob',
            name='howLate',
            field=models.IntegerField(),
        ),
    ]
