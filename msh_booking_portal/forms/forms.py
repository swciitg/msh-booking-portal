from django.forms import ModelForm, DateInput, HiddenInput
from .models import SampleModel, MSHModel
from users.models import SiteUser

class SampleForm(ModelForm):
    class Meta:
        model = SampleModel
        fields = ['charfield', 'textfield']


class MSHForm(ModelForm):
    class Meta:
        model = MSHModel
        fields = ['roll_number',
                  'programme',
                  'department',
                  'address_present',
                  'pincode_present',
                  'phone_number_present',
                  'address_permanent',
                  'pincode_permanent',
                  'phone_number_permanent',
                  'name_of_spouse',
                  'age_of_spouse',
                  'date_of_marriage',
                  'occupation_of_spouse',
                  'place_of_employment_of_spouse',
                  'dependents',
                  'date_by_which_you_intend_to_bring_family',]

        widgets = {
            'date_of_marriage': DateInput(format=('%d/%m/%Y'),
                                            attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'date_by_which_you_intend_to_bring_family': DateInput(format=('%d/%m/%Y'),
                                            attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'dependents': HiddenInput(),
        }



AVAILABLE_FORMS = [SampleForm, MSHForm]
ALL_FORMS = [SampleForm, MSHForm]