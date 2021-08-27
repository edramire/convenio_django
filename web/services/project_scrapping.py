import requests
from bs4 import BeautifulSoup
import re
import time
from random import random
from web.models import Project, Timeline, User
from user_agent import generate_user_agent, generate_navigator

def project_scrapping():
    seconds_sleep = 1
    user = User.objects.get(pk=1)
    url = "https://conveniomarco.mercadopublico.cl/software/publicquotes/requestforquote/lists/?awarded_date=&limit=50&oc=&organization_name=&p=1&quote_id=&quote_name=&service_type=Desarrollo+y+Mantenci%C3%B3n+de+Software&status=1"
    # headers = generate_navigator()
    # headers = {k.title().replace('_','-'):v for k,v in headers.items()}
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    }
    response = requests.get(url,headers=headers)
    print(response.request.headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.select('#wk_mp_requestedquote_table > tbody > tr')
    data = []
    count_created = 0
    count_updated = 0
    print('Rows: {0}'.format(len(rows)))
    if len(rows) == 0:
        print(response.text)
        return []

    for row in rows:
        data_row = {}

        data_row['status'] = 1
        data_row['name'] = row.select('span.name-quote')[0].get_text()
        data_row['code'] = row.select('span.id')[0].get_text()
        data_row['link'] = row.select('a')[0]['href']

        url_detalle = row.select('a')[0]['href']
        response_detalle = requests.get(url_detalle)
        soup_detalle = BeautifulSoup(response_detalle.text, 'html.parser')

        data_row['providers'] = soup_detalle.select(".quantity")[0].get_text();
        data_row['budget'] = soup_detalle.select(".field.amount")[0].span.get_text();
        data_row['deadline'] = soup_detalle.select("span.quote_infolabel")[3].get_text();
        data_row['laravel'] = len(soup_detalle.find_all(text=re.compile("(laravel|Laravel)"))) > 0

        data.append(data_row)

        code = data_row.pop('code')

        print('Adding project code {0}'.format(code))

        project, created = Project.objects.update_or_create(**data_row, defaults={'code': code})
        if created:
            count_created += 1
            project.timeline.create(user=user, status=1)
        else:
            count_updated += 1
            project.timeline.create(user=user, status=2)

        time.sleep(random() * seconds_sleep)

    # codes = [item['code'] for item in data]
    # projects_db = Project.objects.in_bulk(codes, field_name='code')
    # projects_new = [Project(**item) for item in data if not item.code in projects_db]

    # Project.objects.bulk_create(projects_new)
    # Project.objects.bulk_update(projects_db)
    # print('Created: {0} | Updated: {1}'.format(count_created, count_updated))

    return data
