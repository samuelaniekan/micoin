# Generated by Django 3.2 on 2021-05-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0002_alter_account_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='ref_code',
            field=models.CharField(blank=True, default='958', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='refferal',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
