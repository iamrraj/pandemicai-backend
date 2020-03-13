from django.contrib import admin
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin
import csv
from .models import AdminUser, infection, Transport

from django.conf import settings

# Register your models here.


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                   for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class VenueAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ["pk", 'email', 'user', 'location', 'frequency', 'latitude',
                    'longitude']
    search_fields = ('location',)

    fieldsets = (
        (None, {
            'fields': ('user', 'email',  'location', 'frequency', 'latitude',
                       'longitude',)
        }),
    )

    actions = ["export_as_csv"]

    # class Media:
    #     if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
    #         css = {
    #             'all': ('css/admin/location_picker.css',),
    #         }
    #         js = (
    #             'https://maps.googleapis.com/maps/api/js?key={}'.format(
    #                 settings.GOOGLE_MAPS_API_KEY),
    #             'js/admin/location_picker.js',
    #         )


class ProfileAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ["pk", 'start_hour', 'end_hour', 'location', 'address', 'date', 'place_type', 'latitude',
                    'longitude']
    search_fields = ('location',)

    actions = ["export_as_csv"]


class TransportAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ["pk", 'departure_place', 'arrival_place', 'arrival_time',
                    'departure_time', 'transport_number', 'transport_mode', 'date']
    search_fields = ('arrival_place', 'departure_place')
    list_display_links = ('date', 'departure_place', 'arrival_place')
    list_filter = ('transport_mode')

    actions = ["export_as_csv"]


admin.site.register(AdminUser, VenueAdmin)
admin.site.register(infection, ProfileAdmin)
admin.site.register(Transport, TransportAdmin)
