from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    title = models.CharField(_("Title"), max_length=200, )

    class Meta:
        verbose_name = _("Category") 
        verbose_name_plural = _("Categories")

    def __str__(self): 
        return self.title