# Generated by Django 3.1.5 on 2021-02-15 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangogramm', '0005_auto_20210215_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
