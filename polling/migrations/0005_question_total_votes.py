# Generated by Django 3.0.7 on 2020-07-29 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0004_merge_20200729_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='total_votes',
            field=models.IntegerField(default=0),
        ),
    ]