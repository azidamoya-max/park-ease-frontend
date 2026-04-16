from django import forms
from .models import Guest


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'phone_number', 'email_address', 'date_registered']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 0700000000'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g. name@email.com'}),
            'date_registered': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) <= 2:
            raise forms.ValidationError("First name must be more than 2 characters.")
        if not first_name.isalpha():
            raise forms.ValidationError("First name must contain alphabets only.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) <= 2:
            raise forms.ValidationError("Last name must be more than 2 characters.")
        if not last_name.isalpha():
            raise forms.ValidationError("Last name must contain alphabets only.")
        return last_name