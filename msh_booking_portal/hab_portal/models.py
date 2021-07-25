from django.db import models
from users.models import SiteUser

HOSTELS = [
    ('Lohit', 'Lohit'),
    ('Brahmaputra', 'Brahmaputra'),
    ('Siang', 'Siang'),
    ('Manas', 'Manas'),
    ('Disang', 'Disang'),
    ('Kameng', 'Kameng'),
    ('Umiam', 'Umiam'),
    ('Barak', 'Barak'),
    ('Kapili', 'Kapili'),
    ('Dihing', 'Dihing'),
    ('Subansiri', 'Subansiri'),
    ('Dhansiri', 'Dhansiri'),
    ('Married Scholar Hostel', 'Married Scholar Hostel'),
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
        ordering = ['-status','date_of_arrival']

    def __str__(self):
        return self.title
