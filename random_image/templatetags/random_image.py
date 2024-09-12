from django import template

from ..models import ImageContainer

register = template.Library()

@register.simple_tag
def random_image():
    """
    Return a random image.
    """
    return ImageContainer.objects.active().order_by('?').first()
