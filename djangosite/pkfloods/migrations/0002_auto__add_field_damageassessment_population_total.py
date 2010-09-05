# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'DamageAssessment.population_total'
        db.add_column('pkfloods_damageassessment', 'population_total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'DamageAssessment.population_total'
        db.delete_column('pkfloods_damageassessment', 'population_total')


    models = {
        'crowdflower.sms': {
            'Meta': {'object_name': 'SMS'},
            'aliases': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sms': ('django.db.models.fields.TextField', [], {}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'pkfloods.actionable': {
            'Meta': {'object_name': 'Actionable'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'junk_text': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'sms': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crowdflower.SMS']"})
        },
        'pkfloods.damageassessment': {
            'Meta': {'object_name': 'DamageAssessment'},
            'houses_damaged': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'houses_destroyed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pkfloods.Location']", 'null': 'True'}),
            'lost_crops_acres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lost_crops_percentage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lost_livestock': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            'lost_roads': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lost_schools': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'population_adults': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'population_children': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'population_total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sms': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crowdflower.SMS']"}),
            'still_flooded': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'text_houses': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            'text_location': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            'text_notes': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            'text_other_losses': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            'text_population': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'})
        },
        'pkfloods.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unified_council': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pkfloods.UnifiedCouncil']", 'null': 'True'}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pkfloods.Village']", 'null': 'True'})
        },
        'pkfloods.unifiedcouncil': {
            'Meta': {'object_name': 'UnifiedCouncil'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '180'})
        },
        'pkfloods.village': {
            'Meta': {'object_name': 'Village'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'unified_council': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pkfloods.UnifiedCouncil']", 'null': 'True'})
        }
    }

    complete_apps = ['pkfloods']
