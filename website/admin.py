from django.contrib import admin
from .models import ContactUs


# Register your models here.

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'

    def has_add_permission(self, request):
        return False
