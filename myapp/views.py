from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls page.")
def hello(request, username):
    return HttpResponse('<h1>Hello World</h1>')

def projects(request):
    projects1 = list(Project.objects.values())
    return JsonResponse(projects1, safe=False)

def tasks(request, id):
    #task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse('task: %s' % task.title)


