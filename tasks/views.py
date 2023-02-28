from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):
    tasks=Task.objects.all()
    form=TaskForm()

    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")

    context={
        "tasks":tasks,
        'form':form
        }
    return render(request,'tasks/list.html',context=context)

def delete(request,pk):
    item=Task.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect("list")
        
    context={"item":item}
    return render(request,'tasks/delete.html',context)

def update(request,pk):
    task=Task.objects.get(id=pk)    
    form=TaskForm(instance=task)
    form.full_clean()
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)#form da değişiklik yapmana yarıyor
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'tasks/update.html',context)