from multiprocessing.spawn import import_main_path
from django.urls import path,include
from .views import allposts,sigle_post,delepost,editpost,newpost

urlpatterns = [
    path('',allposts,name='allposts'),
    path('<int:id>',sigle_post,name='single'),
    path('<int:id>/edit',editpost,name='editpost'),
    path('<int:id>/delete',delepost,name='deletepost'),
    path('new',newpost,name='new'),
]