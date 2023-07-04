from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from .models import *
from .forms import *

def index(request):
    tasks=task.objects.all()
    form= TaskForm()

    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'tasks':tasks, 'form':form}
    return render(request,'list.html',context)

def updateTask(request,pk):
        tasks=task.objects.get(id=pk)

        form=TaskForm(instance=tasks)

        if request.method=='POST':
            form=TaskForm(request.POST,instance=tasks)
            if form.is_valid():
             form.save()
             return redirect('/')
        context={'form':form}
        return render(request,'update_task.html',context)

def deleteTask(request,pk):
    item=task.objects.get(id=pk)

    if request.method=='POST':
        item.delete()
        return redirect('/')

    context={'item':item}
    return render(request,'delete.html',context)
