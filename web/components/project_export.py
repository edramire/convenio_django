from django_unicorn.components import UnicornView
from web.models import Project
# from services.project_csv_export import project_csv_export

class ProjectExportView(UnicornView):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

    def download_csv(request):
        # data = project_csv_export(request, Project.objects.all())
        # response = HttpResponse(data, content_type='text/csv')
        return data
