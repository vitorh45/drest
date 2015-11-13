from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse as r
from core.forms import TaskForm


def home(request):
	context = {'form': TaskForm()}
	return render(request,'index.html', context)

def add_task(request):
	form = TaskForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(r('home'))
	context = {'form': form}
	return render(request, 'index.html', context)