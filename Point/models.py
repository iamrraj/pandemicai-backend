
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
# from geoposition.fields import GeopositionField


# Create your models here.


MY_CHOICES = (
    ('Single', 'Single'),
    ('Route', 'Route'),
)

TRANSPORT = (
    ('Bus', 'Bus'),
    ('Train', 'Train'),
    ('Flight', 'Flight'),
)


MY_ROUTE = (
    ('Single POI ', 'Single POI'),
    ('List of POIs ', 'List of POIs'),
)


class AdminUser(models.Model):
    user = models.OneToOneField(
        User, models.CASCADE)
    email = models.CharField(
        _("location and region"), max_length=250, blank=True, null=True,)
    first_name = models.CharField(
        _("First Name"), max_length=250, blank=True, null=True)
    last_name = models.CharField(
        _("Last Name"), max_length=250, blank=True, null=True)

    location = models.CharField(
        _("Email of the user"), max_length=250, blank=True, null=True)
    frequency = models.CharField(
        _("frequency"), max_length=250, blank=True, null=True)

    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    # position = GeopositionField()

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, *args, **kwargs):
        if created:
            user_profile = AdminUser(user=instance)
            user_profile.save()


class infection(models.Model):
    date = models.DateField(_("Date of infection"),
                            auto_now=False, auto_now_add=False)
    add_single_point = models.URLField(
        _("Single point link"), max_length=200, default="map.mp")
    add_route_point = models.URLField(
        _("Route point link"), max_length=200, default="route.mp")
    start_hour = models.CharField(
        _("Star Hour"), max_length=100, blank=True, null=True)
    end_hour = models.CharField(
        _("End Hour"), max_length=100, blank=True, null=True)
    address = models.CharField(
        _("Address"), max_length=300, blank=True, null=True)
    name = models.CharField(_("Name"), max_length=100, blank=True, null=True)
    place_type = models.CharField(
        _("Place Type"), max_length=100, blank=True, null=True)
    location = models.CharField(
        _("Location"), max_length=100, blank=True, null=True)
    type = models.CharField(
        _("Place Type"), max_length=100, choices=MY_CHOICES, blank=True, null=True)
    route_id = models.CharField(
        _("Route ID"), max_length=100, choices=MY_ROUTE, blank=True, null=True)

    latitude = models.DecimalField(
        max_digits=10, decimal_places=7, null=True, blank=True)

    longitude = models.DecimalField(
        max_digits=10, decimal_places=7, null=True, blank=True)
    info = models.TextField(_("Info about coronavirus"), null=True, blank=True)


def __str__(self):
    return self.start_hour


class Transport(models.Model):
    date = models.DateField(_("Date of tavel"),
                            auto_now=False, auto_now_add=False)
    arrival_country = models.CharField(_("Transport arrival Country"),
                                       max_length=250, blank=True, null=True)
    departure_country = models.CharField(_("Transport departure Country"),
                                         max_length=250, blank=True, null=True)
    arrival_place = models.CharField(_("Transport arrival city"),
                                     max_length=250, blank=True, null=True)
    departure_place = models.CharField(_("Transport departure city"),
                                       max_length=250, blank=True, null=True)
    arrival_time = models.CharField(_("Transport arrival time"),
                                    max_length=250, blank=True, null=True)
    departure_time = models.CharField(_("Transport departure time"),
                                      max_length=250, blank=True, null=True)
    transport_number = models.CharField(_("Bus train flight number"),
                                        max_length=250, blank=True, null=True)
    transport_mode = models.CharField(_("Mode of transport "),
                                      max_length=250, blank=True, null=True, choices=TRANSPORT)

    def __str__(self):
        return self.arrival_place
