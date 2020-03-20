
from django.contrib import admin
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin
import csv
from .models import CoronaAge, CoronaComorbidity, CoronaSex, Hackathon, Area

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

    export_as_csv.short_description = "Export as CSV"


class AgeAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ["pk",  'age', 'rate']
    list_display_links = ("pk",  'age', 'rate')

    actions = ["export_as_csv"]


class SexAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ["pk",  'sex', 'rate']
    list_display_links = ("pk",  'sex', 'rate')

    actions = ["export_as_csv"]


class ComorbidityAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ["pk",  'condition', 'rate']
    list_display_links = ("pk",  'condition', 'rate')

    actions = ["export_as_csv"]


class DataAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ["pk",  'country', 'totalConfirmed',
                    'totalDeaths', 'totalRecovered', 'province', 'lat', 'long']
    list_display_links = ("pk", 'country', 'totalConfirmed', 'province')
    search_fields = ('country', 'province')

    actions = ["export_as_csv"]


class AreaAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ["pk",  'country', 'totalConfirmed',
                    'totalDeaths', 'totalRecovered', 'displayName', 'lat', 'long']
    list_display_links = ("pk", 'country', 'totalConfirmed', 'displayName')
    search_fields = ('country', 'displayName')

    actions = ["export_as_csv"]


admin.site.register(CoronaAge, AgeAdmin)
admin.site.register(Hackathon, DataAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(CoronaSex, SexAdmin)
admin.site.register(CoronaComorbidity, ComorbidityAdmin)
