from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'posts/(?P<slug>[a-zA-Z]+)/$', views.show_post, name="Entry"),
    url(r'^$', views.index, name="INDEX"),
]
