# Generated by Django 3.2 on 2021-05-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_auto_20210508_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationcode',
            name='code',
            field=models.CharField(max_length=50),
        ),
    ]
