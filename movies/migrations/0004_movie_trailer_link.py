# Generated by Django 2.1.1 on 2018-09-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20180905_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer_link',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
    ]
