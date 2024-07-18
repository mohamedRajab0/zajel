from django.forms import  ModelForm
from django import forms
from.models import *

class MessageForms (ModelForm):
    class Meta:
        model = ZajelMessage
        fields = ['body']
        widget = {
            'body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter message...'}),
        }
        


