from .models import RegisterForm
from django.forms import ModelForm

class RegisterForm(ModelForm):
    class Meta:
        model = RegisterForm
        fields = ['name', 'familia', 'mail', 'login', 'parol']
