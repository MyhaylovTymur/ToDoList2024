from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TodolistItem
from django.http import HttpResponseRedirect
# Create your views here.

def todoappview(request):
    all_todo_item = TodolistItem.objects.all()
    return render(request, 'todolist.html', {'all_items':all_todo_item})


def addTodoView(request):
    x = request.POST['content']
    new_item =  TodolistItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')
