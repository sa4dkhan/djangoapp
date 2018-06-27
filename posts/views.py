from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages


def post_list(request):
    # return HttpResponse("Hello, world. You're at the posts index.")
    posts = Post.objects.all()
    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    # return HttpResponse(str(context))
    return render(request, 'posts/post_list.html', context)


def post_details(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/post_details.html', context)


@login_required(login_url="/accounts/login")
def create_post(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, 'Your post has been successfully saved!')
            return redirect('posts:post_list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/create_post.html', {'form':form})


@login_required(login_url="/accounts/login")
def update_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = forms.CreatePost(request.POST or None, request.FILES, instance=post)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your post has been updated!')
                return redirect('posts:post_details', id)

        except Exception as e:
            messages.warning(request, 'Your post was not saved due to an error: {}'.format(e))
    else:
        form = forms.CreatePost(instance=post)

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'posts/update_post.html', context)



@login_required(login_url="/accounts/login")
def delete_post(request, id):
    post = Post.objects.get(id=id)
    # return HttpResponse(str(post))
    post.delete()
    try:
        messages.success(request, 'Your post has been Deleted!')
        return redirect('posts:post_list')

    except Exception as e:
        messages.warning(request, 'Your post was not deleted due to an error: {}'.format(e))
    return redirect('posts:post_list')


