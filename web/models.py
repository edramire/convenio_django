from django.db.models.fields import related
from .behaviors import Timestampable
from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
# from django.utils.translation import gettext_lazy as _

# from model_utils.models import TimeStampedModel


# class User(AbstractUser):
#     """
#     Usuario que hereda clase por defecto
#     """
#     pass

class Project(Timestampable, models.Model):
    STATUS = (
        (1, 'Publicada'),
        (2, 'Publicación Cerrada'),
        (3, 'En Evaluación'),
        (4, 'Evaluación Cerrada'),
        (5, 'Adjudicada'),
        (6, 'Finalizada'),
        (7, 'Desierta'),
        (8, 'Desestimada'),
    )

    """
    Modelo que representa proyectos convenio marco
    """
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS, default=1)
    providers = models.IntegerField()
    # budget = MoneyField(max_digits=14, decimal_places=2, default_currency='CLP')
    budget = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    deadline = models.DateField(null=True, blank=True)
    laravel = models.BooleanField(default=False)
    # tags = models.BooleanField(default=False)

    def __str__(self):
        """
        String que representa al objeto
        """
        return "{0} - {1}".format(self.code, self.name)

    def last_timeline(self):
        return self.timeline.order_by('-created_at').select_related('asignations').first()
    def last_status(self):
        status = [item[0] for item in Timeline.status_selectable()]
        return self.timeline.filter(status__in=status).order_by('-created_at').first()

class Comment(Timestampable, models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name='comments')
    comment = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return "{0} - {1}".format(self.user, self.project)

class Timeline(Timestampable, models.Model):
    STATUS = [
        (1, 'Descargada'),
        (2, 'Actualizada'),
        (3, 'Rechazada'),
        (4, 'Asignada'),
        (5, 'Postulada'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name='timeline')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='timeline')
    status = models.IntegerField(choices=STATUS, default=1)
    comment = models.TextField(max_length=1000, null=True)

    @property
    def status_name(self):
        return next((x[1] for x in self.STATUS if x[0] == self.status), None)

    def __str__(self):
        return "{0} - {1}".format(self.status_name, self.created_at)

    def status_selectable():
        return Timeline.STATUS[2:]


class Asignation(models.Model):
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE, null=True, related_name='asignations')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='asignations')

class Tag(models.Model):
    name = models.CharField(max_length=255)
    selectors = models.TextField(max_length=1000)

    def __str__(self):
        return "{0} - {1}".format(self.user, self.project)


