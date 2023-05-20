from django.contrib import admin


from apps.users.models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'age', 'phone_number', 'created_at']
    search_fields = ['username', 'age', 'phone_number']
    list_per_page = 20