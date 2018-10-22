from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from .models import Estate


class EstateResource(resources.ModelResource):
    class Meta:
        model = Estate


class EstateAdmin(ImportExportModelAdmin):
    list_display = ('area_name', 'community_name', 'title')
    list_filter = ('city', 'area_name')
    actions = ['SaveExecl']


admin.site.register(Estate, EstateAdmin)
