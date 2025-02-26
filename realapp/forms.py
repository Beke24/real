from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser #if you are using CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser #if you are using CustomUser
        fields = UserCreationForm.Meta.fields + ('email',) # Add any extra fields