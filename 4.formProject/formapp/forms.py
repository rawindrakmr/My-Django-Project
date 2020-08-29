from django import forms

class StudentForm(forms.Form):
    name=forms.CharField()
    mark=forms.IntegerField()
    roll=forms.IntegerField()