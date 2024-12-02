# Generated by Django 4.1.1 on 2024-11-25 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=250)),
                ('status', models.CharField(choices=[('online', 'online'), ('offline', 'offline')], max_length=7)),
                ('img', models.ImageField(default='default_profile.jpg', upload_to='static/images/profile')),
                ('followers', models.ManyToManyField(blank=True, related_name='UserFollowers', to='user.user')),
                ('following', models.ManyToManyField(blank=True, related_name='UserFollowing', to='user.user')),
                ('friends', models.ManyToManyField(blank=True, related_name='UserFriends', to='user.user')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]