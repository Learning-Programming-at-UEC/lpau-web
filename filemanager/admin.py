from django.contrib import admin

from .models import DataFile


class DataFileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'pub_date', )
    list_filter = ['pub_date']


admin.site.register(DataFile, DataFileAdmin)
