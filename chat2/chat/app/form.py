from .models import message,room
from django import forms

class msgform(forms.ModelForm):
    class Meta:
        model = room
        fields = '__all__' 
        
        