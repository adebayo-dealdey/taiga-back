# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_pgjson.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_auto_20150916_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('order', models.IntegerField(verbose_name='order', default=10)),
                ('color', models.CharField(default='#999999', verbose_name='color', max_length=20)),
                ('project', models.ForeignKey(verbose_name='project', related_name='triggers', to='projects.Project')),
            ],
            options={
                'permissions': (('view_trigger', 'Can view trigger'),),
                'verbose_name_plural': 'triggers',
                'verbose_name': 'trigger',
                'ordering': ['project', 'order', 'name'],
            },
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='triggers',
            field=django_pgjson.fields.JsonField(blank=True, verbose_name='triggers', null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='default_trigger',
            field=models.OneToOneField(to='projects.Trigger', verbose_name='default trigger', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+'),
        ),
        migrations.AlterUniqueTogether(
            name='trigger',
            unique_together=set([('project', 'name')]),
        ),
    ]
