from django.contrib import admin

from .models import SampleData, ImageData


# Register your models here.



class SampledataDetail(admin.ModelAdmin):
    list_display = ('mode', 'result', 'test_type', 'patient_id', 'user_id')
    search_fields = ('result', 'patient_id__patient_full_name', 'user_id__username')
    list_filter = ('test_type', 'mode')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ImagedataDetail(admin.ModelAdmin):
    list_display = ('img', 'result', 'sample_data_id')
    search_fields = ('sample_data_id__patient_id__patient_full_name',)
    list_filter = ('result',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(SampleData, SampledataDetail)
admin.site.register(ImageData, ImagedataDetail)
