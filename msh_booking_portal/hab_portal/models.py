import os
from django.db import models
from django.core.exceptions import ValidationError

from users.models import SiteUser

from .storage import OverwriteStorage

HOSTELS = [
    ('Lohit', 'Lohit'),
    ('Brahmaputra', 'Brahmaputra'),
    # add all other hostels
]


def upload_file_name(instance, filename):
    return 'hab_portal/user_{0}.pdf'.format(instance.user.user.username)


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
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)

    time_of_submission = models.DateTimeField(auto_now_add=True)

    roll_number = models.IntegerField('Roll No.')
    hostel = models.CharField('Hostel', max_length=256, choices=HOSTELS)

    date_of_arrival = models.DateField('Date of Arrival')
    fee_paid = models.IntegerField('Fee Paid')
    fee_receipt = models.FileField('Fee Receipt', upload_to=upload_file_name, storage=OverwriteStorage(),
                                   validators=[validate_file_size, validate_file_extension],
                                   help_text='Upload a .PDF file not greater than 10 MB in size.')

    approved = models.BooleanField(default=False)

    locked = models.BooleanField(default=False)


    def __str__(self):
        return self.user.user.username
