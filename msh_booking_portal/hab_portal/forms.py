from django.forms import ModelForm, DateInput, HiddenInput
from .models import HABModel


class HABForm(ModelForm):
    class Meta:
        model = HABModel
        fields = [
                  'roll_number',
                  'hostel',
                  'date_of_arrival',
                  'fee_paid',
                  'fee_receipt',
                  ]

        widgets = {
            'date_of_arrival': DateInput(format='%d/%m/%Y',
                                            attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
        }

        