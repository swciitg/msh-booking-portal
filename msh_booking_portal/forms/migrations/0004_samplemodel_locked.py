# Generated by Django 3.2.5 on 2021-07-15 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_rename_sampleform_samplemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='samplemodel',
            name='locked',
            field=models.BooleanField(default=False),
        ),
    ]
