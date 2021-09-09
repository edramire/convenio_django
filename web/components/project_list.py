from django_unicorn.components import UnicornView
from web.models import Project, Timeline
from datetime import datetime
from django.db.models import Q, Max, F


class ProjectListView(UnicornView):
    projects = []
    deadline = 'actual'
    status_project = 'all'
    status_timeline = 'all'
    status_project_all = []
    status_timeline_all = []
    deadlines_all = [
        ('all', 'Todos los proyectos'),
        ('finished', 'Proyectos pasados'),
        ('actual', 'Proyectos disponibles'),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.status_project_all = Project.STATUS
        self.status_timeline_all = [
            ('all', 'Todos los proyectos'),
            ('not_def', 'Proyectos sin decidir'),
        ] + Timeline.status_selectable()

        self.filter_projects()

    def updated_deadline(self, query):
        self.filter_projects()

    def updated_status_project(self, query):
        self.filter_projects()

    def updated_status_timeline(self, query):
        self.filter_projects()

    def filter_projects(self):
        self.projects = Project.objects.prefetch_related('comments').order_by('deadline')

        if self.deadline != 'all':
            if self.deadline == 'finished':
                self.projects = self.projects.filter(deadline__lt=datetime.now())
            else:
                self.projects = self.projects.filter(deadline__gte=datetime.now())

        if self.status_project != 'all':
            self.projects = self.projects.filter(status=self.status_project)

        if self.status_timeline != 'all':
            if self.status_timeline == 'not_def':
                self.projects = self.projects.annotate(max_timeline=Max('timeline__created_at')).filter(timeline__created_at=F('max_timeline'),timeline__status__in=[1,2])
            else:
                self.projects = self.projects.annotate(max_timeline=Max('timeline__created_at')).filter(timeline__created_at=F('max_timeline'),timeline__status=self.status_timeline)
