from django.db import models

class SMS(models.Model):
    uid = models.CharField(max_length=50)
    sms = models.TextField()
    aliases = models.TextField()