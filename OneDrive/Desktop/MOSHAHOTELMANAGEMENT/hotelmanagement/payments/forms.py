from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['guest', 'room', 'amount', 'payment_type', 'payment_date']
        widgets = {
            'guest': forms.Select(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 150000'}),
            'payment_type': forms.Select(attrs={'class': 'form-control'}),
            'payment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }