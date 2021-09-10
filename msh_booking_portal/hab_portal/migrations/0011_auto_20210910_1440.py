# Generated by Django 3.2.5 on 2021-09-10 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hab_portal', '0010_auto_20210909_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habmodel',
            name='date_of_payment',
            field=models.DateField(default=datetime.datetime.now, null=True, verbose_name='Date of Payment'),
        ),
        migrations.AlterField(
            model_name='habmodel',
            name='email',
            field=models.CharField(max_length=256, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='habmodel',
            name='email_of_supervisor',
            field=models.CharField(blank=True, max_length=256, verbose_name='Supervisor Email'),
        ),
    ]