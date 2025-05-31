from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    title = 'My First Django Project'
    return render(request, 'index.html', {
        'title': title,
    })

def hello(request, username):
    return HttpResponse('<h1>Hello World</h1>')

def projects(request):
    #projects1 = list(Project.objects.values())
    #return JsonResponse(projects1, safe=False)
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects,
    })

def tasks(request, id):
    #task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    #return HttpResponse('task: %s' % task.title)
    return render(request, 'tasks.html')


