from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    latest_posts = Post.objects.order_by('posted_at')

    return HttpResponse("S I E M A ")

#show post by requested slug
def show_post(request, slug):
  post = Post.objects.filter(slug=slug)
  print(post[0].slug)
  # title = post[0].title
  # content = post[0].content
  return HttpResponse(slug)
