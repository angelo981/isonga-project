from django.contrib import admin
from .models import events, Gallery, ContactMessage ,User
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser", "is_active") 

class EventAdmin(admin.ModelAdmin):
    list_display = ("title_en", "event_date", "venue", "is_featured")
    list_filter = ("is_featured", "event_date")
    prepopulated_fields = {"slug": ("title_en",)}

admin.site.register(events, EventAdmin)
admin.site.register(User, UserAdmin)

class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    list_filter = ("category",)

admin.site.register(Gallery, GalleryItemAdmin)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    list_filter = ("created_at",)

admin.site.register(ContactMessage, ContactMessageAdmin)