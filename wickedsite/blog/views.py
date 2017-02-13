from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    return HttpResponse("S I E M A ")

#show post by requested slug
def show_post(request, slug):
    post = Post.objects.filter(slug=slug)
    title = post[0].title
    content = post[0].content
    return HttpResponse("Post :  %s \n    Contewnt : %s" %(title, content) )

