# Generated by Django 5.1.1 on 2024-10-02 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_firstname_user_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
