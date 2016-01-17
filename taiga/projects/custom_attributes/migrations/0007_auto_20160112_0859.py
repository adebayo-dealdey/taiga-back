# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_attributes', '0006_auto_20151014_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuecustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('date', 'Date'), ('select', 'Drop-Down Text')], max_length=16, default='text', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='taskcustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('date', 'Date'), ('select', 'Drop-Down Text')], max_length=16, default='text', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='userstorycustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('date', 'Date'), ('select', 'Drop-Down Text')], max_length=16, default='text', verbose_name='type'),
        ),
    ]
