# Generated by Django 5.0.2 on 2024-02-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('done_or_not', '0005_alter_day_al3asr_alter_day_al3esha_alter_day_aldohr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='alsonan',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='tasbee7',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='the_thousand_pray',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=70, null=True),
        ),
    ]
