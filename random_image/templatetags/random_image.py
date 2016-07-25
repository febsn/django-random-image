# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from ..models import ImageContainer

register = template.Library()

@register.assignment_tag
def random_image():
    """
    Return a random image.
    """
    return ImageContainer.objects.active().order_by('?').first()
