# Generated by Django 3.2 on 2021-05-07 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_withdraw_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='primary_withdraw',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
