# Generated by Django 3.2.5 on 2021-07-26 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hab_portal', '0012_habmodel_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habmodel',
            options={'ordering': ['hostel', '-status', 'date_of_arrival']},
        ),
        migrations.AlterField(
            model_name='habmodel',
            name='hostel',
            field=models.CharField(choices=[('1', 'Lohit'), ('2', 'Brahmaputra'), ('3', 'Siang'), ('4', 'Manas'), ('5', 'Disang'), ('6', 'Kameng'), ('7', 'Umiam'), ('8', 'Barak'), ('9', 'Kapili'), ('10', 'Dihing'), ('11', 'Subansiri'), ('12', 'Dhansiri'), ('13', 'Married Scholar Hostel')], max_length=256, verbose_name='Hostel'),
        ),
    ]