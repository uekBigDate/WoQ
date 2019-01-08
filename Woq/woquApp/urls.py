from django.urls import path
from . import views
app_name = "woqu"

urlpatterns = [
    path("login/",views.login,name="login"),   # 登录功能
    path("register/",views.register,name="register"),   # 注册功能
]