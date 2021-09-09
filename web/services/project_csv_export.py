import csv

# import the relevant model
from web.models import Project, Timeline, User
from django.http import HttpResponse

def project_csv_export(response, queryset):
    model = queryset.model
    model_fields = model._meta.fields + model._meta.many_to_many
    field_names = [field.name for field in model_fields if field != 'id']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="project-export.csv"'

    writer = csv.writer(response, delimiter=";")
    writer.writerow(field_names)
    for row in queryset:
        values = []
        for field in field_names:
            value = getattr(row, field)
            if callable(value):
                try:
                    value = value() or ''
                except:
                    value = 'Error retrieving value'
            if value is None:
                value = ''
            values.append(value)
        writer.writerow(values)
    return response
