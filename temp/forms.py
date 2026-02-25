from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta: 
        model = Student
        fields = ["name", "email", "course"]
        widgets = {
            'name' : forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Full Name'}),
            'email' : forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Enter eamil Address'}),
            'course' : forms.Select(attrs={
                'class':'form-control'})
        }