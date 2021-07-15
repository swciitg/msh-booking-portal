from django.db import models
from users.models import SiteUser

# Create your models here.
class SampleModel(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    charfield = models.CharField(max_length=256, blank=True)
    textfield = models.TextField(blank=True)

    def __str__(self):
        return self.user.user.username + ': ' + self.charfield
