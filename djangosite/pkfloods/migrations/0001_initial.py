# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UnifiedCouncil'
        db.create_table('pkfloods_unifiedcouncil', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('pkfloods', ['UnifiedCouncil'])

        # Adding model 'Village'
        db.create_table('pkfloods_village', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('unified_council', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pkfloods.UnifiedCouncil'], null=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('pkfloods', ['Village'])

        # Adding model 'Location'
        db.create_table('pkfloods_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('village', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pkfloods.Village'], null=True)),
            ('unified_council', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pkfloods.UnifiedCouncil'], null=True)),
        ))
        db.send_create_signal('pkfloods', ['Location'])

        # Adding model 'Actionable'
        db.create_table('pkfloods_actionable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sms', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crowdflower.SMS'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('junk_text', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pkfloods', ['Actionable'])

        # Adding model 'DamageAssessment'
        db.create_table('pkfloods_damageassessment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sms', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crowdflower.SMS'])),
            ('text_location', self.gf('django.db.models.fields.CharField')(max_length=180, blank=True)),
            ('text_population', self.gf('django.db.models.fields.CharField')(max_length=180, blank=True)),
            ('text_houses', self.gf('django.db.models.fields.CharField')(max_length=180, blank=True)),
            ('text_other_losses', self.gf('django.db.models.fields.CharField')(max_length=180, blank=True)),
            ('text_notes', self.gf('django.db.models.fields.CharField')(max_length=180, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pkfloods.Location'], null=True)),
            ('population_adults', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('population_children', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('houses_destroyed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('houses_damaged', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lost_roads', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lost_livestock', self.gf('django.db.models.fields.CharField')(max_length=180, blank=True)),
            ('lost_schools', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lost_crops_acres', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lost_crops_percentage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('still_flooded', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('pkfloods', ['DamageAssessment'])


    def backwards(self, orm):
        
        # Deleting model 'UnifiedCouncil'
        db.delete_table('pkfloods_unifiedcouncil')

        # Deleting model 'Village'
        db.delete_table('pkfloods_village')

        # Deleting model 'Location'
        db.delete_table('pkfloods_location')

        # Deleting model 'Actionable'
        db.delete_table('pkfloods_actionable')

        # Deleting model 'DamageAssessment'
        db.delete_table('pkfloods_damageassessment')


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
