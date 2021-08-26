from django_unicorn.components import UnicornView
from web.models import User, Timeline

class ProjectTimelineView(UnicornView):
    timeline = []
    project_id = 0

    status_all = []
    users_all = []
    users_selected = []
    status_selected = ""
    observations = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.project_id = kwargs.get("project_id")
        self.timeline = Timeline.objects.filter(project__pk=self.project_id)

        self.status_all = Timeline.status_selectable()
        self.users_all = [(user.id, user.username) for user in User.objects.all()]
        self.status_selected = str(self.status_all[0][0])

    def submit_status(self):
        user_id = 1
        newTimeline = Timeline.objects.create(status=self.status_selected, project_id=self.project_id, user_id=user_id, comment=self.observations)

        self.timeline = Timeline.objects.filter(project__pk=self.project_id)
        self.status_selected = str(self.status_all[0][0])
        self.observations = ''
