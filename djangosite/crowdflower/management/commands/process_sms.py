from optparse import make_option

from django.core.management.base import BaseCommand

from crowdflower.models import SMS
from pkfloods.models import Actionable, DamageAssessment

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--no-marking', action='store_true', dest='no_marking', default=False, help='Do not mark SMSs as processed.'),
        make_option('--clobber', action='store_true', dest='clobber', default=False, help='Reprocess previously processed SMSs.'),
        )
    help = 'Parse the fetched SMSs.'

    def handle(self, *args, **options):
        processed = 0
        clobber = options.get('clobber', False)
        no_marking = options.get('no_marking', False)
        verbosity = int(options.get('verbosity', 1))
        for sms in SMS.objects.filter(processed=False):
            if sms.is_actionable():
                if clobber or not Actionable.objects.filter(sms=sms):
                    actionable = Actionable(sms=sms)
                    actionable.process_and_save()
                    processed += 1
            else:
                if clobber or not DamageAssessment.objects.filter(sms=sms):
                    assessment = DamageAssessment(sms=sms)
                    assessment.process_and_save()
                    processed += 1
            if not no_marking:
                sms.processed = True
                sms.save()
        if verbosity:
            print 'Done: %s SMSs processed.' % processed