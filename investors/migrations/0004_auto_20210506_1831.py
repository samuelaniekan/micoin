# Generated by Django 3.2 on 2021-05-06 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0003_auto_20210506_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='reffered_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='ref_code',
            field=models.CharField(blank=True, default='252', max_length=50, null=True),
        ),
    ]