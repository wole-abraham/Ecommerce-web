from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_password2(self):
        return self.cleaned_data.get("password2")
    
    def clean_password1(self):
        return self.cleaned_data.get("password1")
    