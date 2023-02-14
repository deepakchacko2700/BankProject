from django import forms

from bank import settings
from .models import UserDetails, Branch
from django.forms.widgets import DateInput
from django.contrib.admin import widgets


class UserForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ('name', 'DOB', 'age', 'gender', 'Phone_number', 'mail_id',
                  'address', 'district', 'branch', 'account_type',
                  'debit_card', 'credit_card')
        labels = {
            'DOB':'Date of birth',
            'age':'Age'
        }

        widget = {'gender': forms.RadioSelect,
                   'DOB': DateInput,
                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()
        # self.fields['DOB'].widget.attrs['id']
        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('branch')
            except (ValueError, TypeError):
                pass