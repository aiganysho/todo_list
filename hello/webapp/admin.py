from django.contrib import admin
from webapp.models import List
# Register your models here.

# class ListAdmin(admin.ModelAdmin):
class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'describe', 'description', 'date_of_completion']
    list_filter = ['describe']
    search_fields = ['status', 'describe', 'description']
    fields = ['id', 'status', 'describe', 'date_of_completion', 'description']
    readonly_fields = ['id']


admin.site.register(List, ListAdmin)
