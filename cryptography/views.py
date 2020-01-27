from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def index(request):
	posts = Post.objects.all()
	print(posts)
	return render(request, "cryptography/index.html")

def categoryPost(request, categoryInput):
	posts = Post.objects.filter(category=categoryInput)
	return render(request, "cryptography/index.html")

def singlePost(request, slugInput):
	posts = Post.objects.get(slug=slugInput)

	title = "<h1>{}</h1>".format(posts.title)
	body = "<p>{}</p>".format(posts.body)
	#return render(request, "cryptography/index.html")
	return HttpResponse(title + body)