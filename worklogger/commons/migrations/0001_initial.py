# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'commons_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('organisation', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('session_id', self.gf('django.db.models.fields.IntegerField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'commons', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'commons_user')


    models = {
        u'commons.user': {
            'Meta': {'object_name': 'User'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'organisation': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'session_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['commons']