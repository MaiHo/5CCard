# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Flex'
        db.create_table(u'our_app_flex', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('balance', self.gf('django.db.models.fields.FloatField')()),
            ('transaction', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'our_app', ['Flex'])

        # Adding model 'NumMeals'
        db.create_table(u'our_app_nummeals', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mealBalance', self.gf('django.db.models.fields.FloatField')()),
            ('activity', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'our_app', ['NumMeals'])

        # Adding model 'CCash'
        db.create_table(u'our_app_ccash', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('balance', self.gf('django.db.models.fields.FloatField')()),
            ('transaction', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'our_app', ['CCash'])

        # Adding model 'User'
        db.create_table(u'our_app_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('flex', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['our_app.Flex'], unique=True)),
            ('numMeals', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['our_app.NumMeals'], unique=True)),
            ('cCash', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['our_app.CCash'], unique=True)),
        ))
        db.send_create_signal(u'our_app', ['User'])


    def backwards(self, orm):
        # Deleting model 'Flex'
        db.delete_table(u'our_app_flex')

        # Deleting model 'NumMeals'
        db.delete_table(u'our_app_nummeals')

        # Deleting model 'CCash'
        db.delete_table(u'our_app_ccash')

        # Deleting model 'User'
        db.delete_table(u'our_app_user')


    models = {
        u'our_app.ccash': {
            'Meta': {'object_name': 'CCash'},
            'balance': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transaction': ('django.db.models.fields.TextField', [], {})
        },
        u'our_app.flex': {
            'Meta': {'object_name': 'Flex'},
            'balance': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transaction': ('django.db.models.fields.TextField', [], {})
        },
        u'our_app.nummeals': {
            'Meta': {'object_name': 'NumMeals'},
            'activity': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mealBalance': ('django.db.models.fields.FloatField', [], {})
        },
        u'our_app.user': {
            'Meta': {'object_name': 'User'},
            'cCash': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['our_app.CCash']", 'unique': 'True'}),
            'flex': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['our_app.Flex']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numMeals': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['our_app.NumMeals']", 'unique': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['our_app']