from django.contrib import admin
from models import *

class SMSAdmin(admin.ModelAdmin):
    list_display = ('processed', 'uid', 'sms', 'aliases',)
    list_display_links = ('uid',)
    search_fields = ('sms',)

admin.site.register(SMS, SMSAdmin)