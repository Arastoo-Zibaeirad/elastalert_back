# Generated by Django 3.2 on 2021-12-15 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='strategy_alias',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='strategy',
            name='strategy_total',
            field=models.TextField(blank=True, null=True),
        ),
    ]
