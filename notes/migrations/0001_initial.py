# Generated by Django 2.2.7 on 2019-11-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=400)),
                ('company', models.CharField(blank=True, max_length=400)),
                ('day', models.CharField(blank=True, max_length=400)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
