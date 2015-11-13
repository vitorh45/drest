from django import forms
from core.models import Task


class TaskForm(forms.ModelForm):
	
	class Meta:
		model = Task
		fields = ['name', 'is_done']