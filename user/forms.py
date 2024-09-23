from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User
 

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255)

    class Meta:
        model= User
        fields=("email","username","password","password1")