from django.contrib import admin
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin
import csv
from .models import AdminUser, infection

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


# class CsvImportForm(forms.Form):
#     csv_file = forms.FileField()


# class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
#     ...
#     change_list_template = "entities/heroes_changelist.html"

#     def get_urls(self):
#         urls = super().get_urls()
#         my_urls = [
#             ...
#             path('import-csv/', self.import_csv),
#         ]
#         return my_urls + urls

#     def import_csv(self, request):
#         if request.method == "POST":
#             csv_file = request.FILES["csv_file"]
#             reader = csv.reader(csv_file)
#             # Create Hero objects from passed in data
#             # ...
#             self.message_user(request, "Your csv file has been imported")
#             return redirect("..")
#         form = CsvImportForm()
#         payload = {"form": form}
#         return render(
#             request, "admin/csv_form.html", payload
#         )

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


admin.site.register(AdminUser, VenueAdmin)
admin.site.register(infection, ProfileAdmin)
