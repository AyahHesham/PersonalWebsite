from django.shortcuts import render,redirect
from .models import blog

# Create your views here.
def post_list(request):
    posts=blog.objects.all
    return render(request,'blog/post_list.html',{'blog':posts})

def post(request,id):
    post=blog.objects.get(id=id)
    return render(request,'blog/post.html',{'single_post':post})

