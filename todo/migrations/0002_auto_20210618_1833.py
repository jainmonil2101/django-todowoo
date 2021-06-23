# Generated by Django 3.2.3 on 2021-06-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='completed',
        ),
        migrations.AddField(
            model_name='todo',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]