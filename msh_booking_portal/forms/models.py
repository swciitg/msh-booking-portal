from django.db import models
from users.models import SiteUser
from phonenumber_field.modelfields import PhoneNumberField


class SampleModel(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    charfield = models.CharField(max_length=256, blank=True)
    textfield = models.TextField(blank=True)

    locked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.user.username + ': ' + self.charfield


# class MSHModel(models.Model):
#     user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
#
#     roll_number = models.IntegerField()
#     programme = models.CharField(max_length=256)
#     department = models.CharField(max_length=256)
#
#     address_present = models.TextField()
#     pincode_present = models.IntegerField()
#     phone_number_present = PhoneNumberField()
#
#     address_permanent = models.TextField()
#     pincode_permanent = models.IntegerField()
#     phone_number_permanent = PhoneNumberField()
#
#     date_of_marriage = models.DateField()
#     name_of_spouse = models.CharField(max_length=256)
#     age_of_spouse = models.IntegerField()
#     occupation_of_spouse = models.CharField(max_length=256, blank=True)
#     place_of_employment_of_spouse = models.TextField(blank=True)
#
#     date_by_which_you_intend_to_bring_family = models.DateField()
#
#     status = models.CharField(max_length=256)

