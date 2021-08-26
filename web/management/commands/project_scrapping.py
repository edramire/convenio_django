# from web.services.project_scrapping import project_scrapping
import web.services.project_scrapping as pc
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Read projects from server'

    # allows for command line args
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        pc.project_scrapping()
