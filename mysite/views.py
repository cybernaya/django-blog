from django.shortcuts import render

def index(request):
	context = {
		'title':'Home',
		'css':'static/css/styles.css',
		'title_logo':'static/img/logo16x16.png',
		'logo':'static/img/logo.png',
		'banner':'static/img/banner.jpg',
	}
	return render(request, "index.html",context)