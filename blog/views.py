from django.shortcuts import render

from .models import Post

# Create your views here.

def starting_page(request):

    latest_posts = Post.objects.all().order_by("-date")[:3]
    
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    pass


def post_detail(request):
    pass
