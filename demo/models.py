
from django.db import models
from tinymce.models import HTMLField
from datetime import datetime
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.urls import reverse
from markdown_deux import markdown
from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe
# Create your models here.
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class CoronaComorbidity(models.Model):

    condition = models.CharField(
        _("preExistingCondition of patient"), blank=True, null=True, max_length=250)
    rate = models.CharField(
        _("percentage rate of people sex"), blank=True, null=True, max_length=50)

    def __str__(self):
        return self.condition


class CoronaAge(models.Model):
    byage = models.ForeignKey(
        CoronaComorbidity, related_name='byAge', blank=True, on_delete=models.CASCADE)
    age = models.CharField(
        _("Between age of people died"), blank=True, null=True, max_length=250)
    rate = models.CharField(
        _("percentage rate of people age"), blank=True, null=True, max_length=50)

    def __str__(self):
        return self.age


class CoronaSex(models.Model):
    bysex = models.ForeignKey(
        CoronaComorbidity, related_name='bySex', blank=True, on_delete=models.CASCADE)
    sex = models.CharField(
        _("Male or female"), blank=True, null=True, max_length=250)
    rate = models.CharField(
        _("percentage rate of people sex"), blank=True, null=True, max_length=50)

    def __str__(self):
        return self.sex
