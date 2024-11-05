from django import forms
from .models import *
from apps.university.models import *
from choices.varsity.varsity_choices import *

class SessionDetailsForm(forms.ModelForm):
    class Meta:
        model = SessionDetails
        fields = ['session_type', 'session_duration', 'available_dates', 'available_time_slots']
        widgets = {
            'available_dates': forms.DateInput(attrs={'type': 'date'}),
            'available_time_slots': forms.TimeInput(attrs={'type': 'time'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['method', 'transaction_id', 'amount']
        widgets = {
            'method': forms.Select(attrs={'class': 'form-control'}),
            'transaction_id': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class AskUniversityForm(forms.ModelForm):
    class Meta:
        model = AskModel
        fields = ['university', 'department', 'semester', 'course', 'problem_details']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'university' in self.data:
            try:
                university_id = int(self.data.get('university'))
                self.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by('name')
                if 'department' in self.data:
                    department_id = int(self.data.get('department'))
                    semester = int(self.data.get('semester')) if 'semester' in self.data else None
                    self.fields['course'].queryset = Course.objects.filter(department_id=department_id, semester=semester).order_by('title')
            except (ValueError, TypeError):
                pass  # Invalid input - leave queryset empty or set to a default
        
