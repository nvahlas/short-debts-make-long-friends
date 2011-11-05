from django import forms

class AuthenticationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()