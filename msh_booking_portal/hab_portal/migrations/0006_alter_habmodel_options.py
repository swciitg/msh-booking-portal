# Generated by Django 3.2.5 on 2021-07-25 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hab_portal', '0005_auto_20210723_2311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habmodel',
            options={'ordering': ['status', '-date_of_arrival']},
        ),
    ]
