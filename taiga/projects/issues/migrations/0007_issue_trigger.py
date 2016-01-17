# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_auto_20160117_1548'),
        ('issues', '0006_remove_issue_watchers'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='trigger',
            field=models.ForeignKey(verbose_name='trigger', null=True, blank=True, related_name='issues', to='projects.Trigger'),
        ),
    ]
