# Generated by Django 4.1 on 2022-08-24 15:07

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsa_app', '0012_question_posted_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquestion',
            name='posted_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 8, 24, 15, 7, 20, 569843, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userquestion',
            name='your_solution',
            field=ckeditor.fields.RichTextField(default=datetime.datetime(2022, 8, 24, 15, 7, 30, 305854, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]