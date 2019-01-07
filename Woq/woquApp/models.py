from django.db import models
from DB.Base_models import BaseModel
from django.contrib.auth.models import User

# Create your models here.

class News(BaseModel):
    uid = models.ForeignKey(to=User, on_delete=models.CASCADE)
    con = models.CharField(max_length=800, verbose_name='用户动态内容')
    img = models.ImageField(upload_to='news_img', verbose_name='用户动态图片')
    video = models.FileField(upload_to='video', verbose_name='视频')

class Like(BaseModel):
    nid = models.ForeignKey(to=News, on_delete=models.CASCADE)
    uid = models.ForeignKey(to=User, on_delete=models.CASCADE)

class Review(BaseModel):
    nid = models.ForeignKey(to=News, on_delete=models.CASCADE)
    uid = models.ForeignKey(to=User, on_delete=models.CASCADE)
    con = models.CharField(max_length=300, verbose_name='访客回复内容')
    rep = models.CharField(max_length=300, verbose_name='作者回复内容', default='')
