from django.db import models
from users.models import SiteUser

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
    # add all other hostels
]

STATUS = (
    (0,"Approved"),
    (1,"Pending")
)

class HABModel(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)

    time_of_submission = models.DateTimeField(auto_now_add=True)

    roll_number = models.IntegerField('Roll No.')
    hostel = models.CharField('Hostel', max_length=256, choices=HOSTELS)

    date_of_arrival = models.DateField('Date of Arrival')
    fee_paid = models.IntegerField('Fee Paid')
    fee_receipt = models.FileField('Fee Receipt', blank=True)
    status = models.IntegerField(choices=STATUS, default=1)

    approved = models.BooleanField(default=False)

    locked = models.BooleanField(default=False)

    class Meta:
        ordering = ['hostel','-status','date_of_arrival']

    def __str__(self):
        return self.title
