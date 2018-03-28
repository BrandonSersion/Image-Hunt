from django import forms
from account.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

