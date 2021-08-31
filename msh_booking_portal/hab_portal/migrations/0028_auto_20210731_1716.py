# Generated by Django 3.2.5 on 2021-07-31 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_siteuser_data'),
        ('hab_portal', '0027_alter_habmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habmodel',
            name='hostel',
            field=models.CharField(choices=[('1', 'Lohit'), ('2', 'Brahmaputra'), ('3', 'Siang'), ('4', 'Manas'), ('5', 'Disang'), ('6', 'Kameng'), ('7', 'Umiam'), ('8', 'Barak'), ('9', 'Kapili'), ('10', 'Dihing'), ('11', 'Subansiri'), ('12', 'Dhansiri'), ('13', 'Married Scholar Hostel')], max_length=256, null=True, verbose_name='Hostel'),
        ),
        migrations.AlterField(
            model_name='habmodel',
            name='time_of_submission',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='habmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.siteuser'),
        ),
    ]