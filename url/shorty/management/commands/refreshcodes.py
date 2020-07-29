from django.core.management.base import BaseCommand, CommandError
from shorty.models import shortyURL

class Command(BaseCommand):
    help = 'Refreshs all KirrURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        # print(options)
        return shortyURL.objects.refresh_shortcode(items=options['items'])
