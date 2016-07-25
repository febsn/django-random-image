# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField(verbose_name='start date', auto_now_add=True)),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('image', filer.fields.image.FilerImageField(to='filer.Image', related_name='random_image_container')),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
    ]
