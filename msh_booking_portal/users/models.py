from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data = models.TextField(blank=True) # Store the data in JSON format
    # forms_filled = models.ManyToManyField()

    def __str__(self):
        return self.user.username