# Generated by Django 3.2 on 2021-11-27 13:13

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('rule', '0010_alter_rule_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='rule',
            managers=[
                ('default_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
