from django import forms
from .models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'room_category', 'room_status']
        widgets = {
            'room_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 101'}),
            'room_category': forms.Select(attrs={'class': 'form-control'}),
            'room_status': forms.Select(attrs={'class': 'form-control'}),
        }