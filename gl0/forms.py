from django import forms
from django.contrib.auth.forms import AuthenticationForm 

from .models import G

class GForm(forms.ModelForm):

    class Meta:
        model = G
        fields = ('datetime', 'value',)
        
#log/forms.py

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))