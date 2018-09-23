from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Guest

#https://stackoverflow.com/questions/44187640/django-1-11-horizontal-choice-field
class HorizontalRadioRenderer(forms.RadioSelect):
    template_name = 'horizontal_select.html'
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     css_style = 'style="display: inline-block; margin-right: 10px;"'
    #     self.renderer.inner_html = '<li ' + css_style + '>{choice_value}{sub_widgets}</li>'

    # def render(self):
    #  return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class SignUpForm(forms.ModelForm):
    # name = forms.CharField(required=True)
    # last_name = forms.CharField(max_length=30, required=False )
    # email = forms.EmailField(max_length=254, required=True,help_text="*")
    # phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Format: AreaCode+Number - 6592962824.")
    # whatsapp_phone_number = forms.CharField(help_text='Format: 85291790376',max_length=30, validators=[phone_regex]) # validators should be a list
    
    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)
    #     self.fields['comments'].widget = forms.TextInput(attrs={'placeholder': 'Allergies/Children/Others'})
        
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
        fields = ('email','name','whatsapp_number', 'is_attending', 'comments')
        
        # for radio buttons
        # https://stackoverflow.com/questions/30199471/how-to-specify-select-and-radioselect-in-a-modelform
        widgets = {
            'email': forms.TextInput(attrs={'size': 30}),
            'name': forms.TextInput(attrs={'placeholder':'First Name, Last Name','size': 30}),
            'is_attending': HorizontalRadioRenderer,
            'whatsapp_number': forms.TextInput(attrs={'placeholder': 'e.g. 85291790376 (Areacode + number, NO "-"/spaces)', 'size': 50}),
            'comments': forms.TextInput(attrs={'placeholder': 'Allergies/Food Preferences/Children/Others', 'size': 60})
        }