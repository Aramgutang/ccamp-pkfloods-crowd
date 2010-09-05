import simplejson, re, urllib, urllib2

from django.conf import settings
from django.db import models

from crowdflower.models import SMS

LANGUAGES = {
    'en': 'English',
    'ur': 'Urdu',
    'ps': 'Pashto',
    '--': 'Other',
    }

class ProcessedMessage(models.Model):
    sms = models.ForeignKey(SMS)
    
    class Meta:
        abstract = True
    
    def __unicode__(self):
        return self.sms.sms

class UnifiedCouncil(models.Model):
    name = models.CharField(max_length=180)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class Village(models.Model):
    name = models.CharField(max_length=180)
    unified_council = models.ForeignKey(UnifiedCouncil, null=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class Location(models.Model):
    village = models.ForeignKey(Village, null=True)
    unified_council = models.ForeignKey(UnifiedCouncil, null=True)
    
    def __unicode__(self):
        if self.unified_council:
            return '%s, UC %s' % (self.village, self.unified_council)
        else:
            return self.village.name

flrx = re.compile(r'^fl\s*(?P<text>.*)$', re.I)

class Actionable(ProcessedMessage):
    language = models.CharField(max_length=180, choices=LANGUAGES.items(), blank=True)
    junk_text = models.BooleanField(default=False)
    
    def process_and_save(self):
        self.set_language()
        self.detect_junk()
        self.save()
    
    def set_language(self):
        text = self.sms.sms
        if text.lower().startswith('fl'):
            text = flrx.match(text).groups('text')[0]
        key = 'key=%s&' % settings.GOOGLE_API_KEY if hasattr(settings, 'GOOGLE_API_KEY') else  ''
        url = ('http://ajax.googleapis.com/ajax/services/language/detect'
               '?v=1.0&q=%s&%suserip=127.0.0.1' % (urllib.urlencode(text), key))
        request = urllib2.Request(url, None, {'Referer': getattr(settings, 'GOOGLE_API_DOMAIN', 'http://localhost:8000')})
        results = simplejson.load(urllib2.urlopen(request))
        if float(results['responseData']['confidence']) > 0.01:
            language = results['responseData']['language']
            if language in LANGUAGES.keys():
                self.language = language
            else:
                self.language = '--'
    
    def detect_junk(self):
        if len(self.sms.sms) < 10:
            self.junk_text = True
        if 'test' in self.sms.sms and len(self.sms.sms) < 20:
            self.junk_text = True

class DamageAssessment(ProcessedMessage):
    text_location = models.CharField(max_length=180, blank=True)
    text_population = models.CharField(max_length=180, blank=True)
    text_houses = models.CharField(max_length=180, blank=True)
    text_other_losses = models.CharField(max_length=180, blank=True)
    text_notes = models.CharField(max_length=180, blank=True)
    
    location = models.ForeignKey(Location, null=True)
    
    population_total = models.IntegerField(null=True, blank=True)
    population_adults = models.IntegerField(null=True, blank=True)
    population_children = models.IntegerField(null=True, blank=True)
    
    houses_destroyed = models.IntegerField(null=True, blank=True)
    houses_damaged = models.IntegerField(null=True, blank=True)
    
    lost_roads = models.IntegerField(null=True, blank=True, help_text='in km.')
    lost_livestock = models.CharField(max_length=180, blank=True)
    lost_schools = models.IntegerField(null=True, blank=True)
    lost_crops_acres = models.IntegerField(null=True, blank=True)
    lost_crops_percentage = models.IntegerField(null=True, blank=True)
    
    still_flooded = models.NullBooleanField()
    
    def process_and_save(self):
        
        self.save()