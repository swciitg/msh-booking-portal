from django.forms import ModelForm
from .models import SampleModel
from users.models import SiteUser

class SampleForm(ModelForm):
    class Meta:
        model = SampleModel
        fields = ['charfield', 'textfield']

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self._user = kwargs.pop('user')
        super(SampleForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(SampleForm, self).save(commit=False)
        inst.user = SiteUser.objects.get(pk=int(self._user.id))
        if commit:
            inst.save()
            self.save_m2m()
        return inst


AVAILABLE_FORMS = [SampleForm,]