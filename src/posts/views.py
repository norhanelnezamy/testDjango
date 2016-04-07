from django.shortcuts import render,get_object_or_404 , redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Posts
from .forms import CreatePost

def post_list(request):
	posts_data = Posts.objects.all().order_by("-timestamp")
	paginator = Paginator(posts_data, 5)
	#return render(request,"posts/index.html" ,{'posts' : data})
	page = request.GET.get('page')
	try:
	    data = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    data = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    data = paginator.page(paginator.num_pages)

	return render(request, 'posts/index.html', {'posts': data})

def post_details(request,id=None):
	data = get_object_or_404(Posts,id = id)
	return render(request,"posts/details.html" ,{'post' : data})

def post_create(request):
	form = CreatePost(request.POST or None, request.FILES or None)
	if form.is_valid():
		post = form.save()
		post.save()
		return redirect("/post")

	context = { "form" : form }
	return render(request,"posts/create.html" , context )	

def post_update(request,id=None ):
	post = get_object_or_404(Posts,id = id)
	form = CreatePost(request.POST or None, request.FILES or None , instance = post)
	if form.is_valid():
		post = form.save()
		post.save()
		return redirect("/post")

	context = {
	"id":post.id ,
	"title" : post.title ,
	"content" : post.content ,
	"form" : form 
	}
	return render(request,"posts/update.html" , context )

def post_delete(request , id=None):
	post = get_object_or_404(Posts,id = id)
	post.delete()
	return redirect("/post")	