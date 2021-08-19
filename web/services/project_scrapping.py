# Importar módulos
import requests
import csv
from bs4 import BeautifulSoup
import re
import time
from random import random
from web.models import Project

def project_scrapping():
    seconds_sleep = 1

    url = "https://conveniomarco.mercadopublico.cl/software/publicquotes/requestforquote/lists/?awarded_date=&limit=50&oc=&organization_name=&p=1&quote_id=&quote_name=&service_type=Desarrollo+y+Mantenci%C3%B3n+de+Software&status=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.select('#wk_mp_requestedquote_table > tbody > tr')
    data = []

    for row in rows:
        data_row = {}

        data_row['status'] = 1
        data_row['name'] = row.select('span.name-quote')[0].get_text()
        data_row['code'] = row.select('span.id')[0].get_text()
        data_row['link'] = row.select('a')[0]['href']

        # detalle ...
        url_detalle = row.select('a')[0]['href']
        response_detalle = requests.get(url_detalle)
        soup_detalle = BeautifulSoup(response_detalle.text, 'html.parser')

        data_row['providers'] = soup_detalle.select(".quantity")[0].get_text();
        data_row['budget'] = soup_detalle.select(".field.amount")[0].span.get_text();
        data_row['deadline'] = soup_detalle.select("span.quote_infolabel")[3].get_text();
        data_row['laravel'] = len(soup_detalle.find_all(text=re.compile("(laravel|Laravel)"))) > 0

        print(data_row)
        data.append(data_row)
        time.sleep(random() * seconds_sleep)

    # store data
    projects = [Project(**item) for item in data]
    Project.objects.bulk_create(projects)

    return data
