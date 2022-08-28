from django.shortcuts import render
from .models import about

# Create your views here.
def post_list(request):
    posts=about.objects.all
    return render(request,'about.html',{'about':posts})