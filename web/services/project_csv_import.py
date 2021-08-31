# open file & create csvreader
import csv
# import the relevant model
from web.models import Project, Timeline, User

def project_csv_import(path):
    column_names = {
        'estado': 'status',
        'nombre': 'name',
        'codigo': 'code',
        'proveedores': 'link',
        'proveedores': 'providers',
        'presupuesto': 'budget',
        'fecha_cierre': 'deadline',
        'laravel': 'laravel',
    }

    user = User.objects.get(pk=1)

    count_created = 0
    count_updated = 0

    with open(path) as f:
        reader = csv.reader(f, delimiter=';')
        header = next(reader, None)

        # col_pos = {pos: column_names[name] for pos, name in header if column_names[name]}
        # col_pos = {pos: name for pos, name in header}
        print(header)

        for row in reader:
            print(row)
            data_row = {str(header[pos_csv]): row[pos_csv] for pos_csv in range(len(header))}

            code = data_row.pop('code')
            project, created = Project.objects.get_or_create(**data_row, defaults={'code': code})
            if created:
                count_created += 1
                project.timeline.create(user=user, status=1)
            else:
                count_updated += 1
                project.timeline.create(user=user, status=2)
