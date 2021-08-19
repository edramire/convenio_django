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
    context = {
        'project': project,
        'comments': project.comments.select_related('user')
    }
    return render(request, "projects/show.html", context)

# def project_create_comment(request, id):
#     project = Project.objects.get(pk=id)

#     context = {
#         'project': project,
#         'comments': project.comments.select_related('user')
#     }

#     return render(request, "projects/show.html", context)


def project_create_comment(request, id):
    data = json.loads(request.body)
    data['user'] = 1
    data['project'] = id
    form = CommentForm(data)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print(instance)
        res = model_to_dict(instance)
        res['username'] = 'admin'
        return JsonResponse(res, status=201)
    else:
        return JsonResponse(form.errors, safe=False, status=200)


