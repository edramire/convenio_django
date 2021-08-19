from django.db import models
from web.services.project_scrapping import project_scrapping

class ProjectManager(models.Manager):
    def scrapping(self):
        data = project_scrapping()
        projects = [self.model(*item) for item in data]
        self.bulk_create(projects)
