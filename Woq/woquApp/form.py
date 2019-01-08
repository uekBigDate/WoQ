from django.forms import ModelForm,PasswordInput,Form,CharField
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms

class Login(Form):
    name = CharField(widget=forms.TextInput(attrs={"autocomplete":"off","placeholder":"请输入您的账户"}),label="账户")
    password = CharField(widget=forms.PasswordInput(attrs={"placeholder":"请输入您的密码"}),label="密码")

    def clean(self):
        data = super().clean()
        username = data.get('name',None)
        password = data.get('password',None)
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise ValidationError("没有此用户")
            else:
                self.user = user