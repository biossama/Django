from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def all_post(request):
	posts = Post.objects.all()
	return render(request, 'posts/posts_list.html', { 'posts': posts})


def post_page(request, slug):
	post = Post.objects.get(slug=slug)
	return render(request, 'posts/post_slug.html', {'post': post})


@login_required(login_url='/users/login/')
def newPost(request):
	if request.method == "POST":
		form = forms.CreateNewPost(request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.author = request.user
			new_post.save()
			return redirect("posts:post_list")

	else:
		form = forms.CreateNewPost()
	return render(request, 'posts/newPost.html', {'form': form})
