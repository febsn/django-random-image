from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class RandomImageConfig(AppConfig):
    name = 'random_image'
    verbose_name = _("Random images")
