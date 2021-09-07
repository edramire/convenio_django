from web.models import Project
from django.shortcuts import redirect, render
from web.services.project_csv_export import project_csv_export
from web.services.project_csv_import import project_csv_import
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def projects(request):
    context = {
        'projects': Project.objects.prefetch_related('comments').order_by('deadline')
    }
    return render(request, "projects/index.html", context)

@login_required
def project_export_csv(request):
    # if not request.user.is_staff:
    #     raise PermissionDenied
    data = project_csv_export(request, Project.objects.all())
    response = HttpResponse(data, content_type='text/csv')
    return response

@login_required
def show_project(request, id):
    project = Project.objects.get(pk=id)
    last_status = project.last_status()
    context = {
        'project': project,
        'comments': project.comments.select_related('user'),
        'last_status': last_status,
    }
    return render(request, "projects/show.html", context)

@login_required
def project_import_csv(request):
    if not request.method == 'POST' or not 'csv_file' in request.FILES:
        return redirect(reverse('projects'))

    csv_file = request.FILES['csv_file']
    fs = FileSystemStorage()
    filename = fs.save(csv_file.name, csv_file)
    project_csv_import(filename)
    fs.delete(filename)
    return redirect(reverse('projects'))
