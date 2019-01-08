from django.shortcuts import render,redirect,reverse
import json
from django.contrib.auth import login as log
from django.http import HttpResponse

# Create your views here.

# 登录
from .form import Login
def login(request):
    if request.method == "GET":
        form = Login()
        return render(request,"woqu/login.html",{"form":form})
    else:
        form = Login(request.POST)
        if form.is_valid():
            log(request,form.user)
            return redirect(reverse('woqu:login'))
        else:
            return render(request,"woqu/login.html",{"form":form})

# 注册
def register(request):
    return render(request,"woqu/register.html")