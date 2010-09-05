from optparse import make_option, OptionError

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.exceptions import ImproperlyConfigured

from crowdflower import CrowdFlowerFetcher

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--limit', action='store', dest='limit', default=0, help='Only fetch the specified number of SMSs.'),
        )
    help = 'Fetch SMSs from Crowdflower server.'

    def handle(self, *args, **options):
        saved = 0
        limit = options.get('limit', 0)
        verbosity = int(options.get('verbosity', 1))
        try:
            limit = int(limit)
        except ValueError, TypeError:
            raise OptionError('The specified limit "%s" is not a valid number.' % limit, '--limit')
        if not hasattr(settings, 'CROWDFLOWER_URL'):
            raise ImproperlyConfigured('Please specify a CROWDFLOWER_URL in your project settings.')
        if not hasattr(settings, 'CROWDFLOWER_EMAIL'):
            raise ImproperlyConfigured('Please specify a CROWDFLOWER_EMAIL in your project settings.')
        
        fetcher = CrowdFlowerFetcher(settings.CROWDFLOWER_URL, settings.CROWDFLOWER_EMAIL)
        while not limit or saved < limit:
            job = fetcher.fetch_one()
            for line in job.readlines():
                print line
            break
            saved += 1
            print 'Parsed %s' % saved
            if saved > 2:
                break