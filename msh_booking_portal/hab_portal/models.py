from django.db import models
from users.models import SiteUser

HOSTELS = [
    ('Lohit', 'Lohit'),
    ('Brahmaputra', 'Brahmaputra'),
    # add all other hostels
]


class HABModel(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)

    time_of_submission = models.DateTimeField(auto_now_add=True)

    roll_number = models.IntegerField('Roll No.')
    hostel = models.CharField('Hostel', max_length=256, choices=HOSTELS)

    date_of_arrival = models.DateField('Date of Arrival')
    fee_paid = models.IntegerField('Fee Paid')
    fee_receipt = models.FileField('Fee Receipt')

    approved = models.BooleanField(default=False)
