from django.contrib import admin
from models import *

class LocationAdmin(admin.ModelAdmin):
    pass

class ActionableAdmin(admin.ModelAdmin):
    pass

class DamageAssessmentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': ('sms', 'still_flooded',)
        }),
        ('Location', {
            'fields': ('text_location', 'location',)
        }),
        ('Population', {
            'fields': ('text_population', 'population_total', 'population_adults', 'population_children')
        }),
        ('Houses', {
            'fields': ('text_houses', 'houses_destroyed', 'houses_damaged')
        }),
        ('Other losses', {
            'fields': ('text_other_losses', 'lost_roads', 'lost_livestock', 'lost_schools', 'lost_crops_acres', 'lost_crops_percentage')
        }),
    )
    
    readonly_fields = ('sms', 'text_location', 'text_population', 'text_houses', 'text_other_losses')

admin.site.register(Location, LocationAdmin)
admin.site.register(Actionable, ActionableAdmin)
admin.site.register(DamageAssessment, DamageAssessmentAdmin)
