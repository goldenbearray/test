from django import forms

class NameForm(forms.Form):
    intention = forms.CharField(label='User Intention', max_length=200)
