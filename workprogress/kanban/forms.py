from django import forms
from .models import UrgentTask

class UrgentTaskForm(forms.ModelForm):
    class Meta:
        model = UrgentTask
        fields = ['title', 'description']
