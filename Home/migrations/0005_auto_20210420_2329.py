# Generated by Django 3.2 on 2021-04-21 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20210420_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weathertoday',
            name='max_t',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='weathertoday',
            name='min_t',
            field=models.IntegerField(null=True),
        ),
    ]