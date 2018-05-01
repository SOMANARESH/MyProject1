from django import forms

from .models import *



class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32        
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
    phone = forms.CharField(
        required = True,
        label = 'Phone',
        max_length = 32
    )
    location = forms.CharField(max_length=50,
        required = True,
        label = 'Location',
    )
    state = forms.ChoiceField(choices=STATE_CHOICE,
        required=True,
        label = 'State',
    )
    gender = forms.ChoiceField(
        choices = GENDER,
        required = True,
        label = 'Gender',
    )
    
    
#===============================================================================
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
#===============================================================================
        
        
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        state = forms.ModelMultipleChoiceField(queryset = State.objects.all())
        fields = '__all__'
