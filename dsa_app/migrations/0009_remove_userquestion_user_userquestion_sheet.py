# Generated by Django 4.1 on 2022-08-23 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dsa_app', '0008_alter_question_ques_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userquestion',
            name='user',
        ),
        migrations.AddField(
            model_name='userquestion',
            name='sheet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dsa_app.sheet'),
            preserve_default=False,
        ),
    ]
