from django.conf.urls import include, url
from django.urls import path
from web import views as views
from django.views.generic import RedirectView

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", views.dashboard, name="dashboard"),
    url(r"^register/", views.register, name="register"),
    url(r"^projects/list/", views.projects, name="projects"),
    url(r"^projects/(?P<id>[0-9]+)/$", views.show_project, name="project"),
    # url(r"^projects/(?P<id>[0-9]+)/comments/create$", views.project_create_comment, name="project_create_comment"),
    url(r"^projects/import-csv$", views.project_import_csv, name="project_import_csv"),
    url(r"^projects/export-csv$", views.project_export_csv, name="project_export_csv"),
    path('', RedirectView.as_view(url='/projects/list/', permanent=True)),
]
