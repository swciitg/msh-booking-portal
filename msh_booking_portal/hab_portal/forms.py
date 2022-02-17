from django.forms import ModelForm, DateInput, HiddenInput, NumberInput, TextInput,Select, FileInput, RadioSelect
from .models import HABModel, NewHABModel
from .models import PROGRAMME_TO_DATE_RANGE
from datetime import datetime
from django.core.exceptions import ValidationError

class HABForm1(ModelForm):
    class Meta:
        model = HABModel
        fields = ['name',
        'roll_number',
        'gender',
        'email',
        'mobile',
        'vaccination_status',
        'programme',
        'department',
        'supervisor',
        'email_of_supervisor',
        'returning_from_state',
        'vaccination_cert',]


        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                }),

            'roll_number': TextInput(attrs={
                'class': "form-control",
                }),

            'gender': Select(attrs={
                    'class': "form-control",
                    }),
            'department': TextInput(attrs={
                    'class': "form-control",

                }),

            'programme': Select(attrs={

                    'class': "form-control",
                     'id':'prog',
                }),

            'email': TextInput(attrs={
                    'readonly':'readonly',
                    'class': "form-control",
                    'id':'e_mail',
                }),
            'mobile': NumberInput(attrs={
                'class': "form-control",
                }),

            'supervisor': TextInput(attrs={
                    'class': "form-control",
                }),

            'email_of_supervisor': TextInput(attrs={
                    'class': "form-control",
                }),

            'vaccination_status': Select(attrs={
                    'class': "form-control",
                    'id':'vs',
                }),

            'returning_from_state': Select(attrs={
                'class': "form-control",
                }),
    }


class HABdose2(ModelForm):
    class Meta:
        model = HABModel
        fields = [
            'date_of_arrival',
            'mode_of_travel',
            'flight_train_number',
            'nature_of_test',
            'date_of_testing',
            # 'hostel',
            # 'room_no',
            'check_in_date',
            'mess_fee_paid',
            'date_of_payment',
            'fee_receipt',
            'vaccination_cert',
            'travel_ticket',
            # 'rtpcr_report',
        ]


        widgets = {
            'date_of_arrival': DateInput(format='%Y-%m-%d',
                                             attrs={'class':  "form-control",'id':'doa', 'placeholder': 'Select a date',
                                                     'type': 'date'}),
            'date_of_payment': DateInput(format='%Y-%m-%d',
                                             attrs={'class':  "form-control", 'placeholder': 'Select a date',
                                                     'type': 'date'}),
            'date_of_testing': DateInput(format='%Y-%m-%d',
                                              attrs={'class':  "form-control", 'placeholder': 'Select a date',
                                                      'type': 'date'}),
            'check_in_date': DateInput(format='%Y-%m-%d',
                                             attrs={'class':  "form-control", 'placeholder': 'Select a date',
                                                     'type': 'date'}),

            'mode_of_travel': TextInput(attrs={
                     'class': "form-control",
                }),
            'flight_train_number': TextInput(attrs={
                     'class': "form-control",
                }),
            'nature_of_test': Select(attrs={
                     'class': "form-control",
                }),
            # 'hostel': Select(attrs={
            #     'class': "form-control",
            #     }),
            # 'room_no': TextInput(attrs={
            #          'class': "form-control",
            #     }),
            'mess_fee_paid': NumberInput(attrs={
                     'class': "form-control",
                }),
        }


class HABdose1(ModelForm):
    class Meta:
        model = HABModel
        fields = [
            'recieved_an_invite',
            'proof_of_invitation',
        ]

        widgets = {
             'recieved_an_invite': Select(attrs={
                     'class': "form-control",
                 }),
        }


class PdfgeneratedForm(ModelForm):
    class Meta:
        model = HABModel
        fields = [
            'name',
            'roll_number',
            'gender',
            'email',
            'mobile',
            'department',
            'programme',
            'supervisor',
            'email_of_supervisor',
            'vaccination_status',
            'returning_from_state',
            'date_of_arrival',
            'mode_of_travel',
            'flight_train_number',
            'nature_of_test',
            'date_of_testing',
            'hostel',
            'room_no',
            'check_in_date',
            'mess_fee_paid',
            'date_of_payment',
        ]


        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                }),

            'roll_number': NumberInput(attrs={
                'class': "form-control",
                }),

            'gender': Select(attrs={
                    'class': "form-control",
                    }),
            'hostel': Select(attrs={
                'class': "form-control",
                }),
            'department': TextInput(attrs={
                    'class': "form-control",
                }),

            'programme': TextInput(attrs={
                    'class': "form-control",
                }),

            'email': TextInput(attrs={
                    'class': "form-control",
                }),
            'mobile': NumberInput(attrs={
                'class': "form-control",
                }),

            'supervisor': TextInput(attrs={
                    'class': "form-control",
                }),

            'email_of_supervisor': TextInput(attrs={
                    'class': "form-control",
                }),

            'vaccination_status': Select(attrs={
                    'class': "form-control",
                }),

            'date_of_arrival': DateInput(format='%d/%m/%Y',
                                             attrs={'class':  "form-control",'id':'doa', 'placeholder': 'Select a date',
                                                     'type': 'date'}),
            'date_of_payment': DateInput(format='%d/%m/%Y',
                                             attrs={'class':  "form-control", 'placeholder': 'Select a date',
                                                     'type': 'date'}),
            'date_of_testing': DateInput(format='%d/%m/%Y',
                                              attrs={'class':  "form-control", 'placeholder': 'Select a date',
                                                      'type': 'date'}),
            'check_in_date': DateInput(format='%d/%m/%Y',
                                             attrs={'class':  "form-control", 'placeholder': 'Select a date',
                                                     'type': 'date'}),
            'returning_from_state': TextInput(attrs={
                     'class': "form-control",
                }),
            'mode_of_travel': TextInput(attrs={
                     'class': "form-control",
                }),
            'flight_train_number': TextInput(attrs={
                     'class': "form-control",
                }),
            'nature_of_test': Select(attrs={
                     'class': "form-control",
                }),
            'room_no': TextInput(attrs={
                     'class': "form-control",
                }),
            'mess_fee_paid': NumberInput(attrs={
                     'class': "form-control",
                }),
    }


class NewHABForm1(ModelForm):
    class Meta:
        model = NewHABModel
        fields = [
            'name',
            'roll_number',
            'gender',
            # 'email',
            'mobile',
            'vaccination_status',
            'programme',
            'department',
            'supervisor',
            'hostel',
            'room_no',
            'email_of_supervisor',
            'returning_from_state',
            'vaccination_cert',
        ]


        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                }),

            'roll_number': TextInput(attrs={
                'class': "form-control",
                }),

            'gender': Select(attrs={
                    'class': "form-control",
                }),

            'department': TextInput(attrs={
                    'class': "form-control",
                }),

            'programme': Select(attrs={
                    'class': "form-control",
                     'id':'prog',
                }),

            # 'email': TextInput(attrs={
            #         'readonly':'readonly',
            #         'class': "form-control",
            #         'id':'e_mail',
            #     }),

            'mobile': NumberInput(attrs={
                'class': "form-control",
                }),

            'supervisor': TextInput(attrs={
                    'class': "form-control",
                }),

            'email_of_supervisor': TextInput(attrs={
                    'class': "form-control",
                }),
            'hostel': Select(attrs={
                'class': "form-control",
                }),
            'room_no': TextInput(attrs={
                     'class': "form-control",
                }),

            'vaccination_status': Select(attrs={
                    'class': "form-control",
                    'id':'vs',
                }),

            'returning_from_state': Select(attrs={
                'class': "form-control",
                }),
        }

class NewHABdose1(ModelForm):
    class Meta:
        model = HABModel
        fields = [
            'recieved_an_invite',
            'proof_of_invitation',
        ]

        widgets = {
            'recieved_an_invite': Select(attrs={
                'class': "form-control",
            }),
        }

class NewHABForm2(ModelForm):
    class Meta:
        model = HABModel
        fields = [
            'date_of_arrival',
            'mode_of_travel',
            'flight_train_number',
            'nature_of_test',
            'date_of_testing',
            # 'hostel',
            # 'room_no',
            'check_in_date',
            'mess_fee_paid',
            'date_of_payment',
            'fee_receipt',
            # 'vaccination_cert',
            'travel_ticket',
            # 'rtpcr_report',
        ]


        widgets = {
            'date_of_arrival': DateInput(format='%Y-%m-%d',
                                            attrs={'class':  "form-control",'id':'doa', 'placeholder': 'Select a date',
                                                     'type': 'date'}),
            'date_of_payment': DateInput(format='%Y-%m-%d',
                                            attrs={'class':  "form-control", 'placeholder': 'Select a date',
                                                     'type': 'date'}),
            'date_of_testing': DateInput(format='%Y-%m-%d',
                                            attrs={'class':  "form-control", 'placeholder': 'Select a date',
                                                      'type': 'date'}),
            'check_in_date': DateInput(format='%Y-%m-%d',
                                            attrs={'class':  "form-control", 'placeholder': 'Select a date',
                                                     'type': 'date'}),

            'mode_of_travel': TextInput(attrs={
                     'class': "form-control",
                }),
            'flight_train_number': TextInput(attrs={
                     'class': "form-control",
                }),
            'nature_of_test': Select(attrs={
                     'class': "form-control",
                }),
            # 'hostel': Select(attrs={
            #     'class': "form-control",
            #     }),
            # 'room_no': TextInput(attrs={
            #          'class': "form-control",
            #     }),
            'mess_fee_paid': NumberInput(attrs={
                     'class': "form-control",
                }),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = datetime.date(cleaned_data['check_in_date'])
        programme = self.instance.programme
        date_range = PROGRAMME_TO_DATE_RANGE[programme]
        if not (date_range[0] <= check_in_date <= date_range[1]):
            raise ValidationError({'check_in_date': 'According to your programme, your check-in date must be between ' + date_range[0].strftime("%d/%m/%Y") + ' to ' + date_range[1].strftime("%d/%m/%Y") + '.'})
            # self.add_error('check_in_date',
            #                'According to your programme, your check-in date must be between ' + date_range[0].strftime("%d/%m/%Y") + ' to ' + date_range[1].strftime("%d/%m/%Y") + '.')
