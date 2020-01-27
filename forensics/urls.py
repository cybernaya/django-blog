from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),
    url(r'^(?P<categoryInput>[\w-]+)/$',views.categoryPost),
    url(r'^post/(?P<slugInput>[\w-]+)/$',views.singlePost, name='post_forensics'),
]