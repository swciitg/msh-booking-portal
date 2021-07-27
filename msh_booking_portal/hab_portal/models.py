import os
from django.db import models
from django.core.exceptions import ValidationError
from users.models import SiteUser
from .storage import OverwriteStorage

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

STATUS = (
    (0,"Approved"),
    (1,"Pending")
)


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
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)


    time_of_submission = models.DateTimeField(auto_now_add=True)

    roll_number = models.IntegerField('Roll No.')


    hostel = models.CharField('Hostel', max_length=256, choices=HOSTELS)

    date_of_arrival = models.DateField('Date of Arrival')
    fee_paid = models.IntegerField('Fee Paid')
    fee_receipt = models.FileField('Fee Receipt', upload_to=upload_file_name, storage=OverwriteStorage(),
                                   validators=[validate_file_size, validate_file_extension],
                                   help_text='Upload a .PDF file not greater than 10 MB in size.')

    slug = models.SlugField(blank=True)
    status = models.IntegerField(choices=STATUS, default=1)                               

    approved = models.BooleanField(default=False)

    locked = models.BooleanField(default=False)

    class Meta:
        ordering = ['hostel','-status','-time_of_submission']

    def __str__(self):
        return self.user.user.first_name+" "+self.user.user.last_name


