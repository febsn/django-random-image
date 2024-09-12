from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from filer.fields.image import FilerImageField


class ImageContainerManager(models.Manager):
    def active(self):
        return super(ImageContainerManager, self).get_queryset().filter(start_date__lte=now()).filter(
            end_date__gt=now())


class ImageContainer(models.Model):
    start_date = models.DateTimeField(verbose_name=_("start date"))
    end_date = models.DateTimeField(verbose_name=_("end date"))
    image = FilerImageField(related_name=_("random_image_container"), on_delete=models.CASCADE)

    objects = ImageContainerManager()

    class Meta:
        ordering = ['start_date', ]
        verbose_name = _("image")
        verbose_name_plural = _("images")

    def __str__(self):
        return self.image.__str__()
