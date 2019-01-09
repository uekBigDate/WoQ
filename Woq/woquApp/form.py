from django.forms import ModelForm,PasswordInput,Form,CharField, Textarea
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms
from .models import Info, Review

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
                raise ValidationError("用户名或密码错误!")
            else:
                self.user = user

class Register(Form):
    name=CharField(label="用户名",max_length=11,widget=forms.TextInput(attrs={"placeholder":"请在此填写您的手机号码"}))
    def clean(self):
        data = super().clean()
        name = data.get("name", None)
        check=User.objects.filter(username=name).first()
        if check == None:
            length=len(name)
            if length < 11:
                raise ValidationError("手机号不能少于11位")
        else:
            raise ValidationError("用户名已注册")

class Register1(Form):
    name=CharField(label="用户名",max_length=20,widget=forms.TextInput(attrs={"placeholder":"请填写您的用户名"}))
    password = CharField(label="密码",widget=forms.PasswordInput(attrs={"placeholder":"请在此设置您的密码"}))
    password2 = CharField(widget=PasswordInput(attrs={"placeholder":"请再次输入您的密码"}), label="再次输入密码")
    def clean(self):
        data2 = super().clean()
        print("datadata2",data2)
        name2 = data2.get("name", None)
        psd = data2.get("password", None)
        psd2 = data2.get("password2", None)
        print(name2,psd,psd2)
        checkname=Info.objects.filter(nickname=name2).first()
        print(checkname)
        if checkname == None:
            if psd != psd2:
                raise ValidationError("两次密码不一致")
        else:
            raise ValidationError("昵称已存在，请换一个")

class CommentForm(ModelForm):
    class Meta:
        model = Review
        fields = [ 'con', ]
        widgets = {

            'con':Textarea(attrs={'class':"con"}),


        }