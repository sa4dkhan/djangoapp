from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.decorators import login_required
from . import forms


def post_list(request):
    # return HttpResponse("Hello, world. You're at the posts index.")
    posts = Posts.objects.all()[:10]
    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    # return HttpResponse(str(context))
    return render(request, 'posts/index.html', context)


def post_details(request, id):
    post = Posts.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/details.html', context)


@login_required(login_url="/accounts/login")
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/create.html', {'form':form})


