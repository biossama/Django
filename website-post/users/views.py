from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

def register_view(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			auth_login(request, form.save())
			return redirect("/")
	else:
		form = UserCreationForm()
	return render(request, 'users/register.html', {'form': form})


def login_view(request):
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			auth_login(request, form.get_user())
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect("posts:post_list")
	else:
		form = AuthenticationForm()
	return render(request, 'users/login.html', {'form':form})


def logout_view(request):
	auth_logout(request)
	return redirect("users:login_link")
