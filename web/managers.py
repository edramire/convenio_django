from django.db import models
class ProjectManager(models.Manager):
    def last_status(self, project_id: int):
        queryset = self.get_queryset()
        status = [item[0] for item in self.model.status_selectable]
        return queryset.filter(project_id=project_id).filter(status__in=status).order_by('-created_at')[0]
