# Generated by Django 4.0.2 on 2022-03-27 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_question_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='outcome',
        ),
        migrations.RemoveField(
            model_name='question',
            name='response',
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('outcome', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.question')),
            ],
        ),
    ]
