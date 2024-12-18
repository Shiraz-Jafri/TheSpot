# Generated by Django 4.1.1 on 2024-11-25 19:40

from django.db import migrations, models
import django.db.models.deletion
import message.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('population', models.IntegerField(default=1, validators=[message.models.ChatRoom.limit_population])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='user.user')),
                ('visitors', models.ManyToManyField(blank=True, related_name='visitors', to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', max_length=350)),
                ('status', models.CharField(choices=[('Read', 'Read'), ('Delivered', 'Delivered')], max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TextAuthor', to='user.user')),
                ('chatroom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Text', to='message.chatroom')),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TextReciever', to='user.user')),
            ],
        ),
    ]
