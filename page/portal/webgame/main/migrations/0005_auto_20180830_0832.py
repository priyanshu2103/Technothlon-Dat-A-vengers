# Generated by Django 2.1 on 2018-08-30 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_tableset_test_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableset',
            name='test_cal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tableset',
            name='test_store',
            field=models.TextField(default=0),
        ),
    ]
