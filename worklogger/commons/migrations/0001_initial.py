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
            ('session_id', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'commons', ['User'])

        # Adding model 'Project'
        db.create_table(u'commons_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons.User'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'commons', ['Project'])

        # Adding model 'Post'
        db.create_table(u'commons_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons.User'])),
            ('project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons.Project'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('access_type', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal(u'commons', ['Post'])

        # Adding model 'Tag'
        db.create_table(u'commons_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('count', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal(u'commons', ['Tag'])

        # Adding model 'Post_To_Tag'
        db.create_table(u'commons_post_to_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons.Post'])),
            ('tag_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commons.Tag'])),
        ))
        db.send_create_signal(u'commons', ['Post_To_Tag'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'commons_user')

        # Deleting model 'Project'
        db.delete_table(u'commons_project')

        # Deleting model 'Post'
        db.delete_table(u'commons_post')

        # Deleting model 'Tag'
        db.delete_table(u'commons_tag')

        # Deleting model 'Post_To_Tag'
        db.delete_table(u'commons_post_to_tag')


    models = {
        u'commons.post': {
            'Meta': {'object_name': 'Post'},
            'access_type': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commons.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commons.User']"})
        },
        u'commons.post_to_tag': {
            'Meta': {'object_name': 'Post_To_Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commons.Post']"}),
            'tag_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commons.Tag']"})
        },
        u'commons.project': {
            'Meta': {'object_name': 'Project'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commons.User']"})
        },
        u'commons.tag': {
            'Meta': {'object_name': 'Tag'},
            'count': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'commons.user': {
            'Meta': {'object_name': 'User'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'organisation': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'session_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['commons']