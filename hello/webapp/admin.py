from django.contrib import admin
from webapp.models import List
# Register your models here.

# class ListAdmin(admin.ModelAdmin):
class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'describe', 'date_of_completion']
    list_filter = ['describe']
    search_fields = ['status', 'describe']
    fields = ['id', 'status', 'describe', 'date_of_completion']
    readonly_fields = ['date_of_completion', 'id']


admin.site.register(List, ListAdmin)
