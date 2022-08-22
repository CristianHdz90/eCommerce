from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModelMixin(models.Model):
    created = models.DateTimeField(verbose_name=_("created"), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_("modified"), auto_now=True)
    uuid = models.UUIDField()

    class Meta:
        abstract = True
