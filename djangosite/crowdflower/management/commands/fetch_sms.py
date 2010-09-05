import random, time
from optparse import make_option, OptionError

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.exceptions import ImproperlyConfigured

from crowdflower.fetcher import CrowdFlowerFetcher
from crowdflower.parser import CrowdFlowerParser
from crowdflower.models import SMS

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
        if verbosity:
            print 'Logging in to CrowdFlower using email "%s"...' % settings.CROWDFLOWER_EMAIL
            
        fetcher = CrowdFlowerFetcher(settings.CROWDFLOWER_URL, settings.CROWDFLOWER_EMAIL)
        
        if verbosity:
            print 'Log in successful.'
        while not limit or saved < limit:
            job = CrowdFlowerParser(fetcher.fetch_one())
            if not SMS.objects.filter(uid=job.uid).count():
                SMS.objects.create(uid=job.uid, sms=job.sms)
                if verbosity > 1:
                    print '%s: %s' % (job.uid, job.sms)
                saved += 1
            time.sleep(random.randint(0,5))
        if verbosity:
            print 'Done: %s SMSs saved.' % saved