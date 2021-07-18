from django.db import models
from users.models import SiteUser


class SampleModel(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    charfield = models.CharField(max_length=256, blank=True)
    textfield = models.TextField(blank=True)

    locked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.user.username + ': ' + self.charfield


class MSHModel(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)

    time_of_submission = models.DateTimeField(auto_now_add=True)

    roll_number = models.IntegerField('Roll No.')
    programme = models.CharField('Programme', max_length=256)
    department = models.CharField('Department', max_length=256)

    address_present = models.TextField('Present Address')
    pincode_present = models.IntegerField('Pincode')
    phone_number_present = models.IntegerField('Phone Number')

    address_permanent = models.TextField('Permanent Address')
    pincode_permanent = models.IntegerField('Pincode')
    phone_number_permanent = models.IntegerField('Phone Number')

    date_of_marriage = models.DateField('Date of Marriage')
    name_of_spouse = models.CharField('Name of Spouse', max_length=256)
    age_of_spouse = models.IntegerField('Age of Spouse')
    occupation_of_spouse = models.CharField('Occupation of Spouse', max_length=256, blank=True)
    place_of_employment_of_spouse = models.TextField('Place of Employment of Spouse', blank=True)

    dependents = models.TextField('Dependents', blank=True)

    date_by_which_you_intend_to_bring_family = models.DateField('Date by which you intend to bring your Family')

    locked = models.BooleanField(default=False)

    status = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.user.user.username


AVAILABLE_MODELS = [SampleModel, MSHModel]
ALL_MODELS = [SampleModel, MSHModel]
