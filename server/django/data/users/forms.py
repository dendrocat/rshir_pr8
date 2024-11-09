from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        labels = {
            "username": "Логин"
        }
        
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Логин")
    password = forms.CharField(max_length=128,
                               widget=forms.PasswordInput,
                               label="Пароль")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    
class SettingsForm(forms.Form):
    theme = forms.BooleanField(label="Темная тема", required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""