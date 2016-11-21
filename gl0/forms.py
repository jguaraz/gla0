from django import forms

from .models import G

class GForm(forms.ModelForm):

    class Meta:
        model = G
        fields = ('datetime', 'value',)