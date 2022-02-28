from django import forms
from .models import Interface

class InterfaceForm(forms.ModelForm):
    class Meta:
        model = Interface
        fields = ("channel_name" , "username" , "channel_password" , "phone_number" , "email" , "followers")