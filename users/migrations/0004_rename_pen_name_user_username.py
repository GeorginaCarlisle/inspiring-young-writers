# Generated by Django 3.2.23 on 2023-12-06 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pen_name',
            new_name='username',
        ),
    ]
