# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Board'
        db.create_table(u'memento_board', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'memento', ['Board'])

        # Adding model 'Post'
        db.create_table(u'memento_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name')),
            ('board', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memento.Board'])),
        ))
        db.send_create_signal(u'memento', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Board'
        db.delete_table(u'memento_board')

        # Deleting model 'Post'
        db.delete_table(u'memento_post')


    models = {
        u'memento.board': {
            'Meta': {'object_name': 'Board'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'memento.post': {
            'Meta': {'object_name': 'Post'},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['memento.Board']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
        }
    }

    complete_apps = ['memento']