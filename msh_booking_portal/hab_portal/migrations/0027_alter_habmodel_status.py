# Generated by Django 3.2.5 on 2021-07-31 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hab_portal', '0026_alter_habmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habmodel',
            name='status',
            field=models.CharField(choices=[('0', 'Approved'), ('1', 'Pending'), ('-1', 'Rejected')], default='1', max_length=256, null=True),
        ),
    ]