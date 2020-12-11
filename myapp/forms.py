from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Article
from simplemathcaptcha.fields import MathCaptchaField

class RegistrationForm(UserCreationForm):
    captcha = MathCaptchaField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','captcha','password1','password2']

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['name','description','image','privacy']