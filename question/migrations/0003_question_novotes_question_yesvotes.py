# Generated by Django 4.0.2 on 2022-03-27 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_alter_question_dateends_alter_question_dateposted'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='noVotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='yesVotes',
            field=models.IntegerField(default=0),
        ),
    ]
