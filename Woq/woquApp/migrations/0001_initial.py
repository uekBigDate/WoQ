# Generated by Django 2.1.3 on 2019-01-07 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('con', models.CharField(max_length=800, verbose_name='用户动态内容')),
                ('img', models.ImageField(upload_to='news_img', verbose_name='用户动态图片')),
                ('video', models.FileField(upload_to='video', verbose_name='视频')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('con', models.CharField(max_length=300, verbose_name='访客回复内容')),
                ('rep', models.CharField(default='', max_length=300, verbose_name='作者回复内容')),
                ('nid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='woquApp.News')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='like',
            name='nid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='woquApp.News'),
        ),
        migrations.AddField(
            model_name='like',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
