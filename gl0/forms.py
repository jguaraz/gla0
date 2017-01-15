from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User


from .models import G

class GForm(forms.ModelForm):

    class Meta:
        model = G
        fields = ('datetime', 'value',)
        widgets = {'datetime': forms.DateInput(attrs={'id': 'datetimepicker'})}
        
#log/forms.py

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

    
class UserForm(forms.Form):
    username = forms.CharField(label="Username",max_length=30,
                widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                           widget=forms.PasswordInput())
    email=forms.EmailField(required=False)
    first_name = forms.CharField(label="FirstName",max_length=30,
                widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name'}))
    last_name= forms.CharField(label="LastName",max_length=30,
                widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name'}))
    
    def clean_username(self): # check if username dos not exist before
        try:
            User.objects.get(username=self.cleaned_data['username']) #get user from user model
        except User.DoesNotExist :
            return self.cleaned_data['username']
    
        raise forms.ValidationError("this user exist already")
    
    def save(self): # create new user
        new_user=User.objects.create_user(username=self.cleaned_data['username'],
                                        first_name=self.cleaned_data['first_name'],
                                        last_name=self.cleaned_data['last_name'],
                                        password=self.cleaned_data['password'],
                                        email=self.cleaned_data['email'], )
    
        return new_user

