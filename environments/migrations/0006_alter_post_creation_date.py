# Generated by Django 4.2.6 on 2023-11-04 11:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('environments', '0005_rename_action_space_post_actions_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.localdate),
        ),
    ]
