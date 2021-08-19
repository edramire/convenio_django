from django.db import models

class Timestampable(models.Model):
    """
    Agrega timestamp a modelos que hereden de esta clase
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
