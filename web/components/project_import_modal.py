from django_unicorn.components import UnicornView
from web.models import Project
from services.project_csv_import import project_csv_import

class ProjectImportModalView(UnicornView):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

    def import_csv(request):
        # data = project_csv_export(request, Project.objects.all())
        # response = HttpResponse(data, content_type='text/csv')
        return data
