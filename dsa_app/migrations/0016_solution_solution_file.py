# Generated by Django 4.1 on 2022-08-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsa_app', '0015_question_tags_solution_user_userquestion_tag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='solution_file',
            field=models.FileField(default=1, upload_to='uploads/solutions'),
            preserve_default=False,
        ),
    ]
