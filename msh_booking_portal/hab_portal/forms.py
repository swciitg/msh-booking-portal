from django.forms import ModelForm, DateInput, HiddenInput, NumberInput, TextInput,Select, FileInput
from .models import HABModel

class HABForm(ModelForm):
    class Meta:
        model = HABModel
        fields = ['name',
                  'email',
                  'department',
                  'roll_number',
                  'hostel',
                  'date_of_arrival',
                  'fee_to_be_paid',
                  'fee_paid',
                  'date_of_payment',
                  'fee_receipt',]

        widgets = {
            'date_of_arrival': DateInput(format='%d/%m/%Y',
                                            attrs={'class':  "form-control",'id':'doa', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'date_of_payment': DateInput(format='%d/%m/%Y',
                                            attrs={'class':  "form-control", 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'fee_to_be_paid':NumberInput(attrs={'class': "form-control", 'id':'fee', 'readonly': 'readonly'}),
            'name': TextInput(attrs={
                'class': "form-control",
                }),

            'roll_number': NumberInput(attrs={
                'class': "form-control",
                }),
            'hostel': Select(attrs={
                'class': "form-control",
                }),
            'department': TextInput(attrs={
                    'class': "form-control",
                }),
            'email': TextInput(attrs={
                    'class': "form-control",
                }),
            'fee_paid': NumberInput(attrs={
                    'class': "form-control",
                }),
        }
