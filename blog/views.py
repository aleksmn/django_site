from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login

from .forms import RegisterForm
from .models import Post


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автоматически логин
            messages.success(request, 'Регистрация прошла успешно.')
            return redirect('starting-page')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def starting_page(request):

    latest_posts = Post.objects.all().order_by("-date")[:3]
    
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "posts": all_posts
    })


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": post
    })

def about(request):
    return render(request, "blog/about.html")

def contacts(request):
    return render(request, "blog/contacts.html")