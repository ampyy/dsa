# Generated by Django 4.1 on 2022-08-20 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_picture', models.ImageField(blank=True, default='uploads/profile_pictures/default.png', null=True, upload_to='uploads/profile_pictures')),
                ('location', models.CharField(max_length=500)),
                ('about_yourself', models.TextField(blank=True, max_length=1000, null=True)),
                ('profession', models.CharField(blank=True, max_length=500, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=500, null=True)),
                ('linkedin_link', models.CharField(blank=True, max_length=500, null=True)),
                ('github_link', models.CharField(blank=True, max_length=500, null=True)),
                ('portfolio_link', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
