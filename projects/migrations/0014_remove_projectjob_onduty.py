# Generated by Django 2.2.7 on 2019-12-18 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_projectjob_onduty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectjob',
            name='onDuty',
        ),
    ]
