from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, CreateUser, RecordForm, updateForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages
from django.db.models import Q


def home(request):
    return render(request, "webapp/index.html")


def register(request):
	if request.method=="POST":
		form = CreateUser(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "your account was successefull created")
			return redirect("webapp:login-link")
	else:
		form = CreateUser()
	return render(request, 'webapp/register.html', {'form':form})


def login_view(request):
	form = LoginForm()

	if request.method == "POST":
		form = LoginForm(request, data=request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password =  request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect("webapp:dashboard-link")

	return render(request, 'webapp/login.html', {'form':form})


def logout_view(request):
	auth.logout(request)
	messages.success(request, "login out !!")
	return redirect('webapp:login-link')


@login_required(login_url='webapp:login-link')
def dashboard_view(request):
    query = request.GET.get('q')
    if query:
        records = Record.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query) |
            Q(adress__icontains=query) |
            Q(city__icontains=query) |
            Q(province__icontains=query) |
            Q(country__icontains=query)
        )
    else:
        records = Record.objects.all()
    return render(request, 'webapp/dashboard.html', {'records': records})


@login_required(login_url='webapp:login-link')
def create_view(request):
	if request.method == "POST":
		form = RecordForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			messages.success(request, "created successfull")
			return redirect("webapp:dashboard-link")
	else :
		form = RecordForm()
	return render(request, 'webapp/create.html', {'form':form})



def update_view(request, pk):
	record = get_object_or_404(Record, id=pk)
	if request.method == "POST":
		form = updateForm(request.POST, instance=record)
		if form.is_valid():
			form.save()
			messages.success(request, "success updated")
			return redirect('webapp:dashboard-link')
	else:
		form = updateForm(instance=record)
	return render(request, 'webapp/update.html', {'form':form})


def record_view(request, pk):
	record = Record.objects.get(id=pk)
	return render(request, 'webapp/view_record.html', {'record':record})


def delete_view(request, pk):
	record = get_object_or_404(Record, id=pk)
	record.delete()
	messages.success(request, "your record was deleted")
	return redirect('webapp:dashboard-link')









""" my way to create regiter and login auhtentication
from . import forms
from django.contrib.auth import login as auth_login, logout

def home(request):
	return render(request, "webapp/index.html")

def register(request):
	if request.method == "POST":
		form = forms.CreateUser(request.POST)
		if form.is_valid():
			auth_login(request, form.save())
			return redirect("webapp:home-link")
	else:
		form = forms.CreateUser()
	return render(request, 'webapp/register.html', {'form':form})



def login_view(request):
	if request.method == "POST":
		form = forms.LoginForm(data=request.POST)
		if form.is_valid():
			auth_login(request, form.get_user())
			return redirect("webapp:home-link")
	else:
		form = forms.LoginForm()
	return render(request, 'webapp/login.html', {'form':form})


def logout_view(request):
	logout(request)
	return redirect("webapp:home-link")
"""
