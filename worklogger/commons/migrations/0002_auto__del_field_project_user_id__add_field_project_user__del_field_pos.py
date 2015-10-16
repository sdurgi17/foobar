# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.user_id'
        db.delete_column(u'commons_project', 'user_id_id')

        # Adding field 'Project.user'
        db.add_column(u'commons_project', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['commons.User']),
                      keep_default=False)

        # Deleting field 'Post.user_id'
        db.delete_column(u'commons_post', 'user_id_id')

        # Deleting field 'Post.project_id'
        db.delete_column(u'commons_post', 'project_id_id')

        # Adding field 'Post.user'
        db.add_column(u'commons_post', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['commons.User']),
                      keep_default=False)

        # Adding field 'Post.project'
        db.add_column(u'commons_post', 'project',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['commons.Project']),
                      keep_default=False)

        # Deleting field 'Post_To_Tag.post_id'
        db.delete_column(u'commons_post_to_tag', 'post_id_id')

        # Deleting field 'Post_To_Tag.tag_id'
        db.delete_column(u'commons_post_to_tag', 'tag_id_id')

        # Adding field 'Post_To_Tag.post'
        db.add_column(u'commons_post_to_tag', 'post',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['commons.Post']),
                      keep_default=False)

        # Adding field 'Post_To_Tag.tag'
        db.add_column(u'commons_post_to_tag', 'tag',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['commons.Tag']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Project.user_id'
        db.add_column(u'commons_project', 'user_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['commons.User']),
                      keep_default=False)

        # Deleting field 'Project.user'
        db.delete_column(u'commons_project', 'user_id')

        # Adding field 'Post.user_id'
        db.add_column(u'commons_post', 'user_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['commons.User']),
                      keep_default=False)

        # Adding field 'Post.project_id'
        db.add_column(u'commons_post', 'project_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['commons.Project']),
                      keep_default=False)

        # Deleting field 'Post.user'
        db.delete_column(u'commons_post', 'user_id')

        # Deleting field 'Post.project'
        db.delete_column(u'commons_post', 'project_id')

        # Adding field 'Post_To_Tag.post_id'
        db.add_column(u'commons_post_to_tag', 'post_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['commons.Post']),
                      keep_default=False)

        # Adding field 'Post_To_Tag.tag_id'
        db.add_column(u'commons_post_to_tag', 'tag_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['commons.Tag']),
                      keep_default=False)

        # Deleting field 'Post_To_Tag.post'
        db.delete_column(u'commons_post_to_tag', 'post_id')

        # Deleting field 'Post_To_Tag.tag'
        db.delete_column(u'commons_post_to_tag', 'tag_id')


    models = {
        u'commons.post': {
            'Meta': {'object_name': 'Post'},
            'access_type': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commons.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commons.User']"})
        },
        u'commons.post_to_tag': {
            'Meta': {'object_name': 'Post_To_Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commons.Post']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commons.Tag']"})
        },
        u'commons.project': {
            'Meta': {'object_name': 'Project'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commons.User']"})
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