# Generated by Django 2.2.7 on 2019-12-18 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0012_auto_20191218_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectjob',
            name='onDuty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_duty', to=settings.AUTH_USER_MODEL),
        ),
    ]
