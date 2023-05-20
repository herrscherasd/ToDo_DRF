from django.contrib import admin

from apps.tasks.models import ToDo
# Register your models here.
@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_completed', 'created_at']
    search_fields = ['title']
    list_per_page = 20
