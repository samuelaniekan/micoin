# Generated by Django 3.2 on 2021-05-06 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0005_auto_20210506_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='ref_code',
            field=models.CharField(blank=True, default='732', max_length=50, null=True),
        ),
    ]
