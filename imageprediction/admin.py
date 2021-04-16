from django.contrib import admin

from .models import SampleData


# Register your models here.

class Sampledata(admin.ModelAdmin):
    list_display = ('image_name', 'mode', 'result', 'test_type', 'patient_id', 'user_id')
    search_fields = ('result', 'patient_id__patient_full_name', 'user_id__username')
    list_filter = ('test_type', 'mode')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(SampleData, Sampledata)
