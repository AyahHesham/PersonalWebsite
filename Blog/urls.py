from .views import post_list,post
from django.urls import path,include
app_name='blog'

urlpatterns = [
    path('',post_list,name="allposts"),
    path('<int:id>',post,name="singlepost"),
]