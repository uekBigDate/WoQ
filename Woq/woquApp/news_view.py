from django.shortcuts import render, redirect, reverse
from .models import User
from .models import News
from .form_xiaoo import Up_img
import os
import time



def index(request):
    username = request.COOKIES.get('name', None)
    if username:
        return render(request, 'woqu/index.html')
    else:
        return redirect(reverse('woquApp:login'))

def up_news(request):
    username = request.COOKIES['name']
    if request.method == 'POST':
        con = request.POST.get('con', None)
        obj = request.FILES.getlist('img')
        if con or obj:
            uid = User.objects.filter(username=username).first()
            now = str(time.time())[:6]
            path_data = ''
            for img in obj:
                files_path = os.path.join('upload/news_img', (now+img.name))
                _path = os.path.join('news_img', (now+img.name))
                path_data += ('^'+_path)
                f = open(files_path, mode='wb')
                for i in img.chunks():
                    f.write(i)
                f.close()
            News.objects.create(uid=uid, con=con, img=path_data)
            return redirect(reverse('woquApp:news'))  # <-----到动态主页
        up_img = Up_img()
        return render(request, 'woqu/news.html', {'form_img': up_img})
    up_img = Up_img()
    return render(request, 'woqu/news.html', {'form_img': up_img})  # <----------到动态发表页面

def news(request):
    news = News.objects.filter(is_del=0).order_by('-c_time')
    username = request.COOKIES.get('name', None)

    data = {}
    for new in news:
        news_img = new.img.replace('\\', '/')
        news_img = news_img.split('^')
        del news_img[0]
        try:
            has = new.like_set.first().uid.username
            if has != username:
                has = None
            is_del = new.like_set.first().is_del
        except:
            has = None
            is_del = None
        data[new.id] = new.uid, new, news_img, has, is_del

    return render(request, 'woqu/dynamic.html', {'data': data})   #  <----------到动态发表页面
