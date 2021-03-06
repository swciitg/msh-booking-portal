# Generated by Django 3.2.5 on 2021-09-14 13:09

from django.db import migrations, models
import hab_portal.models


class Migration(migrations.Migration):

    dependencies = [
        ('hab_portal', '0017_alter_habmodel_roll_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habmodel',
            options={'ordering': ['hostel', '-status', 'date_of_arrival'], 'permissions': (('can_view_lohit_hostel_data', 'can view lohit hostel data'), ('can_view_brahma_hostel_data', 'can view brahma hostel data'), ('can_view_siang_hostel_data', 'can view siang hostel data'), ('can_view_manas_hostel_data', 'can view manas hostel data'), ('can_view_disang_hostel_data', 'can view disang hostel data'), ('can_view_kameng_hostel_data', 'can view kameng hostel data'), ('can_view_umiam_hostel_data', 'can view umiam hostel data'), ('can_view_barak_hostel_data', 'can view barak hostel data'), ('can_view_kapili_hostel_data', 'can view kapili hostel data'), ('can_view_dihing_hostel_data', 'can view dihing hostel data'), ('can_view_dibang_hostel_data', 'can view dibang hostel data'), ('can_view_suban_hostel_data', 'can view subansiri hostel data'), ('can_view_dhan_hostel_data', 'can view dhansiri hostel data'), ('can_view_msh_hostel_data', 'can view msh hostel data'), ('can_view_not_alloted_data', 'can view not alloted data'))},
        ),
        migrations.AlterField(
            model_name='habmodel',
            name='mobile',
            field=models.IntegerField(verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='habmodel',
            name='roll_number',
            field=models.CharField(help_text='Enter a valid 9 digit Roll Number.', max_length=9, validators=[hab_portal.models.validate_digit_length], verbose_name='Roll No.'),
        ),
    ]
