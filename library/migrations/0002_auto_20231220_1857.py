# Generated by Django 3.2.23 on 2023-12-20 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date_failed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='failed_approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='feedback',
            name='reason_failed',
            field=models.TextField(blank=True, null=True),
        ),
    ]