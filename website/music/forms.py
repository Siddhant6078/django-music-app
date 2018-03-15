from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    """Form definition for User."""
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ['username','email','password']
