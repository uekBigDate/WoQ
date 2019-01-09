from django.contrib.auth import login as log
from woquApp.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .news_view import *
from .form import Login
from .form import Register,Register1,CommentForm
from django.contrib.auth.models import User
from .models import Info,Review
import json


# Create your views here.

# 登录

@csrf_exempt
def login(request):
    if request.method == "GET":
        form = Login()
        return render(request,"woqu/login.html",{"form":form})
    else:
        form = Login(request.POST)
        if form.is_valid():
            log(request,form.user)
            reponse = redirect(reverse('woquApp:index'))
            reponse.set_cookie("name", form.cleaned_data["name"])
            return reponse
        else:
            return render(request,"woqu/login.html",{"form":form})


# 点赞
@csrf_exempt
def send(request):
    message='ok'
    uid = request.user.id
    nid=request.POST.get('nid',None)
    nid1=Like.objects.filter(nid_id=nid,uid_id=uid).first()
    like_num=News.objects.filter(id=nid).first().like_num
    like_num+=1
    if nid1 == None:
        Like.objects.create(nid_id=nid, uid_id=uid, is_del=1)
        News.objects.filter(id=nid).update(like_num=like_num)
    else:
        Like.objects.filter(uid_id=uid).update(is_del=1)
        News.objects.filter(id=nid).update(like_num=like_num)
    return HttpResponse(json.dumps({'message':message}))
# 取消点赞
@csrf_exempt
def back(request):
    message='ok'
    nid=request.POST.get('nid',None)
    uid = request.user.id
    Like.objects.filter(uid_id=uid).update(is_del=0)
    like_num = News.objects.filter(id=nid).first().like_num
    like_num -= 1

    News.objects.filter(id=nid).update(like_num=like_num)
    return HttpResponse(json.dumps({'message':message}))

# 加载注册界面
def register(request):
    if request.method=="POST":
        form = Register(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("data:",data)
            phone=data['name']
            # return render(request, "woqu/register1.html", {'form': form,'phone':phone})
            return redirect(reverse("woquApp:register1"))
            # return render(request, "woqu/register.html", {'form': form})
        else:
            return render(request,"woqu/register.html",{'form':form})
    else:
        form = Register()
        return render(request,"woqu/register.html",{'form':form})

# 加载填写信息页面
def register1(request):
    if request.method=="POST":
        form = Register1(request.POST)

        if form.is_valid():
            data2 = form.cleaned_data
            # print("data2:", data2)
            nickname=data2['name']
            password=data2['password']
            phone=request.POST.get('phone',None)
            User.objects.create_user(username=phone,password=password)
            id=User.objects.filter(username=phone).first().id
            Info.objects.create(nickname=nickname,user_id=id)
            form = Login()
            return render(request, "woqu/login.html", {'form': form})
        else:
            return render(request, "woqu/register1.html", {'form': form})
    else:
        form2 = Register1()
        return render(request,"woqu/register1.html", {'form': form2})

def detail(request):
    username = request.user.username
    comment=Review.objects.all()
    print(comment)

    return render(request,'woqu/wx_detail.html',{'comment':comment,'username':username})

def comment(request, nid):
    print(nid)
    username=request.user.username
    uid=User.objects.filter(username=username).first().id
    if request.method=="GET":
        form=CommentForm()
        return render(request, 'woqu/wx_comment.html', {'form': form, 'nid': nid})
    else:
        form=CommentForm(request.POST)
        if form.is_valid():
            Review.objects.create(**form.cleaned_data,uid_id=uid,nid_id=nid)
            '''还需要news表   review_num +1 '''   #  <------------------------------------
            return redirect(reverse("woquApp:news"))
        return render(request,'woqu/wx_comment.html',{'form':form})

def zhuye(request):
    return render(request,'woqu/wx_zhuye.html')