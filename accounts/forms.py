from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Profile
from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError
from datetime import date


class CustomUserCreationForm(UserCreationForm):
    dob = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        required=False,
        label='Date of Birth'
    )
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('dob','email','phone')
    
    def clean_dob(self):
        dob = self.cleaned_data['dob']
        today = date.today()
        if dob > today:
            raise ValidationError('Must enter a valid date of birth.',code='invalid')
        
        return dob
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not str(phone).isdigit() or len(phone) < 10:
            raise ValidationError('Must enter a valid phone number.',code='invalid')



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','dob','phone')


class CustomProfileChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('fname','lname','biography','picture')
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'biography': 'Biography',
            'picture': 'Profile Picture',
        }

