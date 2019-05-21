from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.sessions.models import Session
from datetime import datetime
from django.contrib import messages
# date = datetime.now()
# print(date)

def index(request):
    context = {
        "show": Shows.objects.all()
    }
    # print('*' * 80)
    # print(context)
    return render(request, "show/index.html", context)

def newshow(request):
    return render(request, "show/newshow.html")

def addshow(request):
    errors = Shows.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/newshow')
    if request.method == "POST":
        show = Shows.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['date'], descriptions=request.POST['description'])
        # print('*' * 80)
        messages.success(request, "Show successfully added!")
        # print(show)
    return redirect(f'show/{show.id}')

def show(request, num):
    id=num
    context = {
        "show": Shows.objects.get(id=id)
    }
    # print(context)
    return render(request, "show/show.html", context)

def edit(request, num):
    id=num
    request.session['id'] = id
    context = {
        "show": Shows.objects.get(id=id)
    }
    # print(context)
    return render(request, "show/edit.html", context)

def editshow(request):
    id = request.session['id']
    errors = Shows.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{id}')
    else:
        if request.method == "POST":
            show = Shows.objects.get(id=id)
            # print(show.title)
            show.title = request.POST['title']
            # print(show.title)
            # print(show.network)
            show.network = request.POST['network']
            # print(show.network)
            # print(show.release_date)
            show.release_date = request.POST['date']
            # print(show.release_date)
            show.descriptions = request.POST['description']
            show.save()
            # print('*' * 80)
            # print(show)
            messages.success(request, "Show successfully editted!")
    return redirect(f"show/{id}")

def destroy(request, num):
    id=num
    s = Shows.objects.get(id=id)
    s.delete()
    return redirect('/')