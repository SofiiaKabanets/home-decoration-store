from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
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
        age_limit = today.replace(year=today.year - 13)

        if dob and dob > age_limit:
            raise ValidationError(gettext_lazy('You must be 13 years old or older to register.'))
        
        return dob


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','dob','phone')