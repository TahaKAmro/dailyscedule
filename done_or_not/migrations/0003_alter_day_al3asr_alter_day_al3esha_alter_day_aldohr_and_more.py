# Generated by Django 5.0.2 on 2024-02-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('done_or_not', '0002_day_alsonan_day_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='Al3asr',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='Al3esha',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='Aldohr',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='Alfajr',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='Almaghrib',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='alsonan',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='daily_quraan',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='tasbee7',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='the_thousand_pray',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
