# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'SMS.date_seen'
        db.add_column('crowdflower_sms', 'date_seen', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 9, 5, 15, 9, 30, 500000)), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'SMS.date_seen'
        db.delete_column('crowdflower_sms', 'date_seen')


    models = {
        'crowdflower.sms': {
            'Meta': {'object_name': 'SMS'},
            'aliases': ('django.db.models.fields.TextField', [], {}),
            'date_seen': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sms': ('django.db.models.fields.TextField', [], {}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['crowdflower']
