# Generated by Django 3.2 on 2021-12-02 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule', '0021_alter_strategy_rules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategy',
            name='rules',
            field=models.ManyToManyField(to='rule.Rule'),
        ),
    ]
