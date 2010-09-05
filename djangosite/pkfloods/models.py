from django.db import models

from crowdflower.models import SMS

LANGUAGES = ['English', 'Urdu', 'Pashtun', 'Other',]

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

class Actionable(models.Model):
    sms = models.ForeignKey(SMS)
    language = models.CharField(max_length=180, choices=zip(LANGUAGES, LANGUAGES))
    junk_text = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.sms.sms

class DamageAssessment(models.Model):
    sms = models.ForeignKey(SMS)
    
    text_location = models.CharField(max_length=180, blank=True)
    text_population = models.CharField(max_length=180, blank=True)
    text_houses = models.CharField(max_length=180, blank=True)
    text_other_losses = models.CharField(max_length=180, blank=True)
    text_notes = models.CharField(max_length=180, blank=True)
    
    location = models.ForeignKey(Location, null=True)
    
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
    
    def __unicode__(self):
        return self.sms.sms