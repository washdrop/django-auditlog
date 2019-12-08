# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields.jsonb
import django.core.serializers.json


class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0004_logentry_detailed_object_repr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='additional_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='additional data', blank=True),
        ),
    ]
