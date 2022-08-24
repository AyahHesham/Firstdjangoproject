from multiprocessing.sharedctypes import Value
from django.shortcuts import render , redirect
from .models import post
from .form import formpost
# Create your views here.
def allposts(request):
    posts=post.objects.all
    return render(request,'post.html',{'aya':posts})

def sigle_post(request,id):
    posts=post.objects.get(id=id)
    return render(request,'single.html',{'single_post':posts})

def newpost(request):
    if request.method=='POST':
        form=formpost(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/posts/')
    else:
        form=formpost()
    return render(request,'newpost.html',{'form':form})

def editpost(request,id):
    posts=post.objects.get(id=id)
    if request.method=='POST':
        form=formpost(request.POST,instance=posts)
        if form.is_valid():
            form.save()
        return redirect('/posts')
    else:
        form=formpost(instance=posts)
    return render(request,'edit.html',{'form':form})
def delepost(request,id):
    posts=post.objects.get(id=id)
    posts.delete()
    return redirect('/posts')


    
