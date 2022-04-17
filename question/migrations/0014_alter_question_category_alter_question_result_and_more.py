# Generated by Django 4.0.3 on 2022-04-10 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0013_results_alter_question_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='question.category'),
        ),
        migrations.AlterField(
            model_name='question',
            name='result',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='question.results'),
        ),
        migrations.AlterField(
            model_name='results',
            name='result',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None),
        ),
    ]