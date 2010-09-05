# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SMS'
        db.create_table('crowdflower_sms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sms', self.gf('django.db.models.fields.TextField')()),
            ('aliases', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('crowdflower', ['SMS'])


    def backwards(self, orm):
        
        # Deleting model 'SMS'
        db.delete_table('crowdflower_sms')


    models = {
        'crowdflower.sms': {
            'Meta': {'object_name': 'SMS'},
            'aliases': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sms': ('django.db.models.fields.TextField', [], {}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['crowdflower']
