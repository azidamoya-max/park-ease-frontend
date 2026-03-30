from django import forms
from .models import Student

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'is_present', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }