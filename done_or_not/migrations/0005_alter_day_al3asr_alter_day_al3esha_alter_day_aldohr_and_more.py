# Generated by Django 5.0.2 on 2024-02-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('done_or_not', '0004_alter_day_al3asr_alter_day_al3esha_alter_day_aldohr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='Al3asr',
            field=models.CharField(choices=[('Done in mosque', 'Yes in mosque'), ('Done but not in mosque', 'Yes/no mosque'), ('Done but not in mosque and late', 'Yes/no mosque + late'), ("Done but qada'", "Yes/no mosque + qada'"), ("Wasn't done", 'NO')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='Al3esha',
            field=models.CharField(choices=[('Done in mosque', 'Yes in mosque'), ('Done but not in mosque', 'Yes/no mosque'), ('Done but not in mosque and late', 'Yes/no mosque + late'), ("Done but qada'", "Yes/no mosque + qada'"), ("Wasn't done", 'NO')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='Aldohr',
            field=models.CharField(choices=[('Done in mosque', 'Yes in mosque'), ('Done but not in mosque', 'Yes/no mosque'), ('Done but not in mosque and late', 'Yes/no mosque + late'), ("Done but qada'", "Yes/no mosque + qada'"), ("Wasn't done", 'NO')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='Alfajr',
            field=models.CharField(choices=[('Done in mosque', 'Yes in mosque'), ('Done but not in mosque', 'Yes/no mosque'), ('Done but not in mosque and late', 'Yes/no mosque + late'), ("Done but qada'", "Yes/no mosque + qada'"), ("Wasn't done", 'NO')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='Almaghrib',
            field=models.CharField(choices=[('Done in mosque', 'Yes in mosque'), ('Done but not in mosque', 'Yes/no mosque'), ('Done but not in mosque and late', 'Yes/no mosque + late'), ("Done but qada'", "Yes/no mosque + qada'"), ("Wasn't done", 'NO')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='alsonan',
            field=models.CharField(choices=[('Done in mosque', 'Yes in mosque'), ('Done but not in mosque', 'Yes/no mosque'), ('Done but not in mosque and late', 'Yes/no mosque + late'), ("Done but qada'", "Yes/no mosque + qada'"), ("Wasn't done", 'NO')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='daily_quraan',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='tasbee7',
            field=models.CharField(choices=[('Done in mosque', 'Yes in mosque'), ('Done but not in mosque', 'Yes/no mosque'), ('Done but not in mosque and late', 'Yes/no mosque + late'), ("Done but qada'", "Yes/no mosque + qada'"), ("Wasn't done", 'NO')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='the_thousand_pray',
            field=models.CharField(choices=[('Done in mosque', 'Yes in mosque'), ('Done but not in mosque', 'Yes/no mosque'), ('Done but not in mosque and late', 'Yes/no mosque + late'), ("Done but qada'", "Yes/no mosque + qada'"), ("Wasn't done", 'NO')], max_length=70, null=True),
        ),
    ]
