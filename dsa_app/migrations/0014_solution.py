# Generated by Django 4.1 on 2022-08-24 16:06

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dsa_app', '0013_userquestion_posted_time_userquestion_your_solution'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', ckeditor.fields.RichTextField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dsa_app.userquestion')),
            ],
        ),
    ]