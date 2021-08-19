from django.db.models.fields import related
from .behaviors import Timestampable
from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
# from .managers import ProjectManager
from django.utils.translation import gettext_lazy as _

# from model_utils.models import TimeStampedModel


# class User(AbstractUser):
#     """
#     Usuario que hereda clase por defecto
#     """
#     pass

class Project(Timestampable, models.Model):
    # objects = ProjectManager
    STATUS = (
        (1, _('Publicada')),
        (2, _('Publicación Cerrada')),
        (3, _('En Evaluación')),
        (4, _('Evaluación Cerrada')),
        (5, _('Adjudicada')),
        (6, _('Finalizada')),
        (7, _('Desierta')),
        (8, _('Desestimada')),
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

    def __str__(self):
        """
        String que representa al objeto
        """
        return "{0} - {1}".format(self.code, self.name)


class Comment(Timestampable, models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='users')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name='comments')
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return "{0} - {1}".format(self.user, self.project)

