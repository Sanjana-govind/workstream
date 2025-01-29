from django import forms
from .models import UrgentTask
from .models import Task

class UrgentTaskForm(forms.ModelForm):
    class Meta:
        model = UrgentTask
        fields = ['title', 'description']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority']
        widgets = {
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }
