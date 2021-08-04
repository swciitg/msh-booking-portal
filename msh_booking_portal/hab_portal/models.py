import os
from django.db import models
from django.core.exceptions import ValidationError
from users.models import SiteUser
from .storage import OverwriteStorage
from django.contrib.auth.models import User

HOSTELS = [
    ('1', 'Lohit'),
    ('2', 'Brahmaputra'),
    ('3', 'Siang'),
    ('4', 'Manas'),
    ('5', 'Disang'),
    ('6', 'Kameng'),
    ('7', 'Umiam'),
    ('8', 'Barak'),
    ('9', 'Kapili'),
    ('10', 'Dihing'),
    ('11', 'Subansiri'),
    ('12', 'Dhansiri'),
    ('13', 'Married Scholar Hostel'),
]

STATUS = [
    ('Accepted','Accepted'),
    ('Pending','Pending'),
    ('Declined','Declined'),
]

def upload_file_name(instance, filename):
    return 'hab_portal/user_{0}.pdf'.format(instance.user.pk)


def validate_file_size(value):
    size = value.size

    if size <= 10*1024**2:
        return value
    else:
        raise ValidationError('The maximum file size is 10 MB.')


def validate_file_extension(value):
    if os.path.splitext(value.name)[-1] == '.pdf':
        return value
    else:
        raise ValidationError('Upload a PDF File.')


class HABModel(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE, null=True, blank=True)

    time_of_submission = models.DateTimeField(auto_now_add=True, null=True)

    roll_number = models.IntegerField('Roll No.', null=True)


    hostel = models.CharField('Hostel', max_length=256, choices=HOSTELS, null=True)

    date_of_arrival = models.DateField('Date of Arrival', null=True)
    fee_paid = models.IntegerField('Fee Paid', null=True)
    fee_receipt = models.FileField('Fee Receipt', upload_to=upload_file_name, storage=OverwriteStorage(), null=True,
                                   validators=[validate_file_size, validate_file_extension],
                                   help_text='Upload a .PDF file not greater than 10 MB in size.')

    slug = models.SlugField(null=True, blank=True)
    status = models.CharField(max_length=256, choices=STATUS, default='Pending', null=True)                               

    approved = models.BooleanField(default=False, null=True)

    locked = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ['hostel','-status','date_of_arrival']
        permissions = (
            ('can_view_lohit_hostel_data', 'can view lohit hostel data'),
            ('can_view_brahma_hostel_data', 'can view brahma hostel data'),
            ('can_view_siang_hostel_data', 'can view siang hostel data'),
            ('can_view_manas_hostel_data', 'can view manas hostel data'),
            ('can_view_disang_hostel_data', 'can view disang hostel data'),
            ('can_view_kameng_hostel_data', 'can view kameng hostel data'),
            ('can_view_umiam_hostel_data', 'can view umiam hostel data'),
            ('can_view_barak_hostel_data', 'can view barak hostel data'),
            ('can_view_kapili_hostel_data', 'can view kapili hostel data'),
            ('can_view_dihing_hostel_data', 'can view dihing hostel data'),
            ('can_view_suban_hostel_data', 'can view subansiri hostel data'),
            ('can_view_dhan_hostel_data', 'can view dhansiri hostel data'),
            ('can_view_msh_hostel_data', 'can view msh hostel data'),
        )

    def __str__(self):
        return self.user.user.first_name+" "+self.user.user.last_name


