from django.shortcuts import render
from djangoapp.models import Post

# Create your views here.

def base(request):
    return render (request,  'djangoapp/base.html')


def post(request):

    posts= Post.objects.all()

    context = {
        "all_posts":posts,
    }
    return render(request,"djangoapp/index.html",context)

def detail(request,pk):

    post= Post.objects.get(pk=pk)

    body= {
        "post":post,
    }
    return render(request,"djangoapp/detail.html",body)

def gallery (request):
    return render(request, "djangoapp/gallery.html")
