from django.forms import ModelForm
from .models import SampleModel
from users.models import SiteUser

class SampleForm(ModelForm):
    class Meta:
        model = SampleModel
        fields = ['charfield', 'textfield']


AVAILABLE_FORMS = [SampleForm,]