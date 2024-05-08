from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def index(request):
	todo = Todo.objects.all()
	if request.method == 'POST':
		new_todo = request.POST.get('title')
		new_todo = Todo(title=new_todo)
		new_todo.save()
		return redirect('/')
	return render(request, 'index.html', {'todos': todo})


def delete(request, pk):
	todo = Todo.objects.get(id=pk)
	todo.delete()
	return redirect('/')
