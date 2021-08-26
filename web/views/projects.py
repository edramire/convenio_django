from web.models import Project
from django.shortcuts import redirect, render
from web.forms import CommentForm
from django.forms import model_to_dict
from django.http import JsonResponse
import json

def projects(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, "projects/index.html", context)

def show_project(request, id):
    project = Project.objects.get(pk=id)
    last_status = project.last_status()
    context = {
        'project': project,
        'comments': project.comments.select_related('user'),
        'last_status': last_status,
    }
    return render(request, "projects/show.html", context)

