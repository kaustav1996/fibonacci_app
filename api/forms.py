from django import forms

class FiboForm(forms.Form):
    n = forms.IntegerField(label='Enter a Number')