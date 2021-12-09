from django import forms
from .models import ExerciseModel
 
 
class ExerciseForm(forms.ModelForm):
 
    class Meta:
        model = ExerciseModel
 
        fields = [
            "title",
        ]