# -*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from models import BlogPost
from django.template import loader,Context
from django.http import HttpResponse
# Create your views here.

#def archive(request): ##方法一较繁琐
#    posts = BlogPost.objects.all()
#    t = loader.get_template('archive.html')
#    c = Context({'posts' : posts}) ##html li de bianliang
#    return HttpResponse(t.render(c))

def archive(resquest): #方法2 较简单
    posts = BlogPost.objects.all()
    return render_to_response('archive.html',{'posts' : posts})

