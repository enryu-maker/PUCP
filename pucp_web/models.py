from cProfile import label
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserData(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("LOGIN DATA")
        verbose_name_plural = _("LOGIN DATA")


    def __str__(self):
        return self.username
# Create your models here.
