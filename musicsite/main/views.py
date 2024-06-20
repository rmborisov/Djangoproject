from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MusicTask
from .forms import MusicTaskForm

#def index(request):
#    return HttpResponse("<h4>Hello</h4>")

def index(request):
    tasks = MusicTask.objects.order_by('-id')
    return render(request,'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def singers(request):
    return render(request,'main/singers.html')

def create(request):
    error =''
    if request.method == 'POST':
        form = MusicTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = MusicTaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request,'main/create.html', context)