# Generated by Django 4.1.1 on 2024-11-25 19:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoRoom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('creator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='VideoCallAuthor', to='user.user')),
                ('members', models.ManyToManyField(related_name='VideoRoomMembers', to='user.user')),
            ],
        ),
    ]