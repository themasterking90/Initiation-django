# Generated by Django 2.1.5 on 2019-02-03 12:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutoriel',
            name='tutoriel_publier',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 3, 13, 19, 26, 117557), verbose_name='date publiée'),
        ),
    ]
