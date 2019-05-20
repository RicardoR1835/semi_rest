from django.shortcuts import render, HttpResponse, redirect
from apps.show.models import *
from django.contrib.sessions.models import Session
from datetime import datetime

def index(request):
    context = {
        "show": Shows.objects.all()
    }
    print('*' * 80)
    print(context)
    return render(request, "show/index.html", context)

def newshow(request):
    return render(request, "show/newshow.html")

def addshow(request):
    if request.method == "POST":
        show = Shows.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['date'], descriptions=request.POST['description'])
        print('*' * 80)
        print(show)
    return redirect(f'show/{show.id}')

def show(request, num):
    id=num
    context = {
        "show": Shows.objects.get(id=id)
    }
    print(context)
    return render(request, "show/show.html", context)

def edit(request, num):
    id=num
    context = {
        "show": Shows.objects.get(id=id)
    }
    print(context)
    return render(request, "show/edit.html", context)

def destroy(request, num):
    id=num
    s = Shows.objects.get(id=id)
    s.delete()
    return redirect('/')