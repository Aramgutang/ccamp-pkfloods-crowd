from django.db import models

class SMS(models.Model):
    uid = models.CharField(max_length=50)
    sms = models.TextField()
    aliases = models.TextField()
    processed = models.BooleanField(default=False)
    date_seen = models.DateTimeField()
    
    class Meta:
        verbose_name = 'SMS'
        verbose_name_plural = 'SMSs'
    
    def __unicode__(self):
        return self.sms
    
    def is_actionable(self):
        return not self.sms.startswith('Initial Damage Assessment:')