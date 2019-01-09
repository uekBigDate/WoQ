from django.urls import path
from . import news_view
from . import views

app_name = 'woquApp'

urlpatterns = [
    path('',news_view.index, name = 'index'),
    path("login/",views.login,name="login"),   #登录功能
    path('up_news/', news_view.up_news, name='up_news'),  # 发表动态
    path('news/', news_view.news, name='news'),  # 动态
    path('send/',views.send,name='send'),   # 点赞
    path('back/',views.back,name='back'),   # 撤回赞

    path('register/',views.register,name="register"),
    path('register1/',views.register1,name="register1"),
    path('detail/',views.detail,name="detail"),
    path('zhuye/',views.zhuye,name="zhuye"),
    path('comment/<nid>',views.comment,name="comment"),
]