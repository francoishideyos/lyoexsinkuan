from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Guest

class SignUpForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=30, required=False )
    # last_name = forms.CharField(max_length=30, required=False )
    # email = forms.EmailField(max_length=254, required=True,help_text="*")
    # phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Format: AreaCode+Number - 6592962824.")
    # whatsapp_phone_number = forms.CharField(help_text='Format: 85291790376',max_length=30, validators=[phone_regex]) # validators should be a list
    
    # def __init__(self, *args, **kwargs):
        # super(SignUpForm, self).__init__(*args, **kwargs)
        
        # https://stackoverflow.com/questions/14299039/django-how-to-remove-the-password-field-from-the-usercreationform/14301395
        # del self.fields['password1']
        # del self.fields['password2']

        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
        # self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        # self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    class Meta:
    	# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
        model = Guest
        fields = ('email','first_name', 'last_name','whatsapp_phone_number')