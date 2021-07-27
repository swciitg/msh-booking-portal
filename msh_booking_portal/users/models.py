from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data = models.TextField(default='{}', blank=True) # Store the data in JSON format
    # forms_filled = models.ManyToManyField()

    # the data attribute stores all the extra data we have about the user
    # from previously filled forms as a JSON Object
    # The JSON Object is stored as a string and needs to be converted
    # before usage.

    def __str__(self):
        return self.user.username
