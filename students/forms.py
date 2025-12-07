from django import forms

class StudentForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=15)