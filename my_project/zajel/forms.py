from django.forms import  ModelForm
from.models import *

class MessageForms (ModelForm):
    class Meta:
        model = ZajelMessage
        fields = ['body']

