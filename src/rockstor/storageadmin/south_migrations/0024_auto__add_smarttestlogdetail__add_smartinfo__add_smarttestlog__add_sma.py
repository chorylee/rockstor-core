# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SMARTTestLogDetail'
        db.create_table(u'storageadmin_smarttestlogdetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['storageadmin.SMARTInfo'])),
            ('line', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('storageadmin', ['SMARTTestLogDetail'])

        # Adding model 'SMARTInfo'
        db.create_table(u'storageadmin_smartinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('disk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['storageadmin.Disk'])),
            ('toc', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('storageadmin', ['SMARTInfo'])

        # Adding model 'SMARTTestLog'
        db.create_table(u'storageadmin_smarttestlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['storageadmin.SMARTInfo'])),
            ('test_num', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('pct_completed', self.gf('django.db.models.fields.IntegerField')()),
            ('lifetime_hours', self.gf('django.db.models.fields.IntegerField')()),
            ('lba_of_first_error', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('storageadmin', ['SMARTTestLog'])

        # Adding model 'SMARTErrorLogSummary'
        db.create_table(u'storageadmin_smarterrorlogsummary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['storageadmin.SMARTInfo'])),
            ('error_num', self.gf('django.db.models.fields.IntegerField')()),
            ('lifetime_hours', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('etype', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('storageadmin', ['SMARTErrorLogSummary'])

        # Adding model 'SMARTAttribute'
        db.create_table(u'storageadmin_smartattribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['storageadmin.SMARTInfo'])),
            ('aid', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('flag', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('normed_value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('worst', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('threshold', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('atype', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('raw_value', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('updated', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('failed', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('storageadmin', ['SMARTAttribute'])

        # Adding model 'SMARTIdentity'
        db.create_table(u'storageadmin_smartidentity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['storageadmin.SMARTInfo'])),
            ('model_family', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('device_model', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('world_wide_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('firmware_version', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('capacity', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('sector_size', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('rotation_rate', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('in_smartdb', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('ata_version', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('sata_version', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('scanned_on', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('supported', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('enabled', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('assessment', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('storageadmin', ['SMARTIdentity'])

        # Adding model 'SMARTCapability'
        db.create_table(u'storageadmin_smartcapability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['storageadmin.SMARTInfo'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('flag', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('capabilities', self.gf('django.db.models.fields.CharField')(max_length=2048)),
        ))
        db.send_create_signal('storageadmin', ['SMARTCapability'])

        # Adding model 'SMARTErrorLog'
        db.create_table(u'storageadmin_smarterrorlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['storageadmin.SMARTInfo'])),
            ('line', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('storageadmin', ['SMARTErrorLog'])

        # Adding field 'Disk.smart_available'
        db.add_column(u'storageadmin_disk', 'smart_available',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Disk.smart_enabled'
        db.add_column(u'storageadmin_disk', 'smart_enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'SMARTTestLogDetail'
        db.delete_table(u'storageadmin_smarttestlogdetail')

        # Deleting model 'SMARTInfo'
        db.delete_table(u'storageadmin_smartinfo')

        # Deleting model 'SMARTTestLog'
        db.delete_table(u'storageadmin_smarttestlog')

        # Deleting model 'SMARTErrorLogSummary'
        db.delete_table(u'storageadmin_smarterrorlogsummary')

        # Deleting model 'SMARTAttribute'
        db.delete_table(u'storageadmin_smartattribute')

        # Deleting model 'SMARTIdentity'
        db.delete_table(u'storageadmin_smartidentity')

        # Deleting model 'SMARTCapability'
        db.delete_table(u'storageadmin_smartcapability')

        # Deleting model 'SMARTErrorLog'
        db.delete_table(u'storageadmin_smarterrorlog')

        # Deleting field 'Disk.smart_available'
        db.delete_column(u'storageadmin_disk', 'smart_available')

        # Deleting field 'Disk.smart_enabled'
        db.delete_column(u'storageadmin_disk', 'smart_enabled')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'oauth2_provider.application': {
            'Meta': {'object_name': 'Application'},
            'authorization_grant_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'client_id': ('django.db.models.fields.CharField', [], {'default': "u'6yI=42rlI1ZRmW0bPEY9O_7HfAzdecHOVs;VkQOV'", 'unique': 'True', 'max_length': '100'}),
            'client_secret': ('django.db.models.fields.CharField', [], {'default': "u'GYOauegLbg;sCctbbLg_fqPVUp@wxZnlqFFlv!xSfeDxV:@gY3kANcN646ul.X-9v=Sx=swQ0Rm.WlOGWPDF3ux-aDHx46h6tUhikJ8?i?5vRkibylmZ:OJfwZzNm@AT'", 'max_length': '255', 'blank': 'True'}),
            'client_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'redirect_uris': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'storageadmin.advancednfsexport': {
            'Meta': {'object_name': 'AdvancedNFSExport'},
            'export_str': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'storageadmin.apikeys': {
            'Meta': {'object_name': 'APIKeys'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'user': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '8'})
        },
        'storageadmin.appliance': {
            'Meta': {'object_name': 'Appliance'},
            'client_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'client_secret': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'current_appliance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hostname': ('django.db.models.fields.CharField', [], {'default': "'Rockstor'", 'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4096'}),
            'mgmt_port': ('django.db.models.fields.IntegerField', [], {'default': '443'}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'storageadmin.containeroption': {
            'Meta': {'object_name': 'ContainerOption'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.DContainer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'val': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'storageadmin.dashboardconfig': {
            'Meta': {'object_name': 'DashboardConfig'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'widgets': ('django.db.models.fields.CharField', [], {'max_length': '4096'})
        },
        'storageadmin.dcontainer': {
            'Meta': {'object_name': 'DContainer'},
            'dimage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.DImage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.DContainer']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1024'}),
            'rockon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.RockOn']"})
        },
        'storageadmin.dcustomconfig': {
            'Meta': {'unique_together': "(('rockon', 'key'),)", 'object_name': 'DCustomConfig'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'rockon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.RockOn']"}),
            'val': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'})
        },
        'storageadmin.dimage': {
            'Meta': {'object_name': 'DImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'repo': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'storageadmin.disk': {
            'Meta': {'object_name': 'Disk'},
            'btrfs_uuid': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'offline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parted': ('django.db.models.fields.BooleanField', [], {}),
            'pool': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.Pool']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'size': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'smart_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'smart_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transport': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'})
        },
        'storageadmin.dport': {
            'Meta': {'unique_together': "(('container', 'containerp'),)", 'object_name': 'DPort'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.DContainer']"}),
            'containerp': ('django.db.models.fields.IntegerField', [], {}),
            'hostp': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protocol': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'})
        },
        'storageadmin.dvolume': {
            'Meta': {'unique_together': "(('container', 'dest_dir'),)", 'object_name': 'DVolume'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.DContainer']"}),
            'dest_dir': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'share': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.Share']", 'null': 'True'}),
            'uservol': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'storageadmin.group': {
            'Meta': {'object_name': 'Group'},
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gid': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'groupname': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'storageadmin.installedplugin': {
            'Meta': {'object_name': 'InstalledPlugin'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'install_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'plugin_meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.Plugin']"})
        },
        'storageadmin.iscsitarget': {
            'Meta': {'object_name': 'IscsiTarget'},
            'dev_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'dev_size': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'share': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.Share']"}),
            'tid': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'tname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'storageadmin.netatalkshare': {
            'Meta': {'object_name': 'NetatalkShare'},
            'description': ('django.db.models.fields.CharField', [], {'default': "'afp on rockstor'", 'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4096'}),
            'share': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'netatalkshare'", 'unique': 'True', 'to': "orm['storageadmin.Share']"}),
            'time_machine': ('django.db.models.fields.CharField', [], {'default': "'yes'", 'max_length': '3'})
        },
        'storageadmin.networkinterface': {
            'Meta': {'object_name': 'NetworkInterface'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'boot_proto': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'dns_servers': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'gateway': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipaddr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'itype': ('django.db.models.fields.CharField', [], {'default': "'io'", 'max_length': '100'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'netmask': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'network': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'onboot': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        'storageadmin.nfsexport': {
            'Meta': {'object_name': 'NFSExport'},
            'export_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.NFSExportGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mount': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'share': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.Share']"})
        },
        'storageadmin.nfsexportgroup': {
            'Meta': {'object_name': 'NFSExportGroup'},
            'admin_host': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'editable': ('django.db.models.fields.CharField', [], {'default': "'rw'", 'max_length': '2'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'host_str': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mount_security': ('django.db.models.fields.CharField', [], {'default': "'insecure'", 'max_length': '8'}),
            'nohide': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'syncable': ('django.db.models.fields.CharField', [], {'default': "'async'", 'max_length': '5'})
        },
        'storageadmin.oauthapp': {
            'Meta': {'object_name': 'OauthApp'},
            'application': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['oauth2_provider.Application']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.User']"})
        },
        'storageadmin.plugin': {
            'Meta': {'object_name': 'Plugin'},
            'css_file_name': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4096'}),
            'display_name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '4096'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'js_file_name': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4096'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4096'})
        },
        'storageadmin.pool': {
            'Meta': {'object_name': 'Pool'},
            'compression': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mnt_options': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4096'}),
            'raid': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'size': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'toc': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        'storageadmin.poolbalance': {
            'Meta': {'object_name': 'PoolBalance'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percent_done': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pid': ('django.db.models.fields.IntegerField', [], {}),
            'pool': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.Pool']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'started'", 'max_length': '10'})
        },
        'storageadmin.poolscrub': {
            'Meta': {'object_name': 'PoolScrub'},
            'corrected_errors': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'csum_discards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'csum_errors': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'data_extents_scrubbed': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kb_scrubbed': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'last_physical': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'malloc_errors': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'no_csum': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pid': ('django.db.models.fields.IntegerField', [], {}),
            'pool': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.Pool']"}),
            'read_errors': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'started'", 'max_length': '10'}),
            'super_errors': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tree_bytes_scrubbed': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'tree_extents_scrubbed': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'uncorrectable_errors': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'unverified_errors': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'verify_errors': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'storageadmin.posixacls': {
            'Meta': {'object_name': 'PosixACLs'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'perms': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'smb_share': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.SambaShare']"})
        },
        'storageadmin.rockon': {
            'Meta': {'object_name': 'RockOn'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True'})
        },
        'storageadmin.sambacustomconfig': {
            'Meta': {'object_name': 'SambaCustomConfig'},
            'custom_config': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'smb_share': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.SambaShare']"})
        },
        'storageadmin.sambashare': {
            'Meta': {'object_name': 'SambaShare'},
            'browsable': ('django.db.models.fields.CharField', [], {'default': "'yes'", 'max_length': '3'}),
            'comment': ('django.db.models.fields.CharField', [], {'default': "'foo bar'", 'max_length': '100'}),
            'guest_ok': ('django.db.models.fields.CharField', [], {'default': "'no'", 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4096'}),
            'read_only': ('django.db.models.fields.CharField', [], {'default': "'no'", 'max_length': '3'}),
            'share': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'sambashare'", 'unique': 'True', 'to': "orm['storageadmin.Share']"})
        },
        'storageadmin.setup': {
            'Meta': {'object_name': 'Setup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'setup_disks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'setup_network': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'setup_system': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'setup_user': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'storageadmin.sftp': {
            'Meta': {'object_name': 'SFTP'},
            'editable': ('django.db.models.fields.CharField', [], {'default': "'ro'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'share': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['storageadmin.Share']", 'unique': 'True'})
        },
        'storageadmin.share': {
            'Meta': {'object_name': 'Share'},
            'compression_algo': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'root'", 'max_length': '4096'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4096'}),
            'owner': ('django.db.models.fields.CharField', [], {'default': "'root'", 'max_length': '4096'}),
            'perms': ('django.db.models.fields.CharField', [], {'default': "'755'", 'max_length': '9'}),
            'pool': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.Pool']"}),
            'qgroup': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'replica': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'size': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'subvol_name': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'toc': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        'storageadmin.smartattribute': {
            'Meta': {'object_name': 'SMARTAttribute'},
            'aid': ('django.db.models.fields.IntegerField', [], {}),
            'atype': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'failed': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'flag': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.SMARTInfo']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'normed_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'raw_value': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'threshold': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'worst': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'storageadmin.smartcapability': {
            'Meta': {'object_name': 'SMARTCapability'},
            'capabilities': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'flag': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.SMARTInfo']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'storageadmin.smarterrorlog': {
            'Meta': {'object_name': 'SMARTErrorLog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.SMARTInfo']"}),
            'line': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'storageadmin.smarterrorlogsummary': {
            'Meta': {'object_name': 'SMARTErrorLogSummary'},
            'details': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'error_num': ('django.db.models.fields.IntegerField', [], {}),
            'etype': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.SMARTInfo']"}),
            'lifetime_hours': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'storageadmin.smartidentity': {
            'Meta': {'object_name': 'SMARTIdentity'},
            'assessment': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'ata_version': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'capacity': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'device_model': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'enabled': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'firmware_version': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_smartdb': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.SMARTInfo']"}),
            'model_family': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'rotation_rate': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sata_version': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'scanned_on': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sector_size': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'supported': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'world_wide_name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'storageadmin.smartinfo': {
            'Meta': {'object_name': 'SMARTInfo'},
            'disk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.Disk']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'toc': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'storageadmin.smarttestlog': {
            'Meta': {'object_name': 'SMARTTestLog'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.SMARTInfo']"}),
            'lba_of_first_error': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'lifetime_hours': ('django.db.models.fields.IntegerField', [], {}),
            'pct_completed': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'test_num': ('django.db.models.fields.IntegerField', [], {})
        },
        'storageadmin.smarttestlogdetail': {
            'Meta': {'object_name': 'SMARTTestLogDetail'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.SMARTInfo']"}),
            'line': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'storageadmin.snapshot': {
            'Meta': {'unique_together': "(('share', 'name'),)", 'object_name': 'Snapshot'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'qgroup': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'real_name': ('django.db.models.fields.CharField', [], {'default': "'unknownsnap'", 'max_length': '4096'}),
            'share': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.Share']"}),
            'size': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'snap_type': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '64'}),
            'toc': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uvisible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'writable': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'storageadmin.supportcase': {
            'Meta': {'object_name': 'SupportCase'},
            'case_type': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'zipped_log': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'storageadmin.tlscertificate': {
            'Meta': {'object_name': 'TLSCertificate'},
            'certificate': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1024'})
        },
        'storageadmin.user': {
            'Meta': {'object_name': 'User'},
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'gid': ('django.db.models.fields.IntegerField', [], {'default': '5000'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storageadmin.Group']", 'null': 'True'}),
            'homedir': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public_key': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'null': 'True'}),
            'shell': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'smb_shares': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'admin_users'", 'null': 'True', 'to': "orm['storageadmin.SambaShare']"}),
            'uid': ('django.db.models.fields.IntegerField', [], {'default': '5000'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'suser'", 'unique': 'True', 'null': 'True', 'to': u"orm['auth.User']"}),
            'username': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '4096'})
        }
    }

    complete_apps = ['storageadmin']