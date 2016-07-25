# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class RandomImageConfig(AppConfig):
    name = 'random_image'
    verbose_name = _("Random images")
