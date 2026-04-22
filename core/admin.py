from django.contrib import admin
from .models import Event, Gallery, ContactMessage, User, Blog, Talent, Category, ProgramApplication

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser", "is_active")


class EventAdmin(admin.ModelAdmin):
    list_display = ("title_en", "event_date", "venue", "is_featured")
    search_fields = ("title_en", "venue")
    list_filter = ("event_date", "is_featured")
    prepopulated_fields = {"slug": ("title_en",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    search_fields = ("title", "category")
    list_filter = ("category", "created_at")


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "sub_content", "content")
    list_filter = ("created_at",)
    prepopulated_fields = {"slug": ("title",)}


class TalentAdmin(admin.ModelAdmin):
    list_display = ("title", "is_featured", "created_at")
    search_fields = ("title", "sub_content", "content")
    list_filter = ("is_featured", "created_at")
    prepopulated_fields = {"slug": ("title",)}


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at", "name", "email", "subject", "message")
    
    def has_add_permission(self, request):
        return False


class ProgramApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "program_interest", "created_at")
    list_filter = ("program_interest", "created_at")
    search_fields = ("full_name", "email", "why_join", "experience")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)


admin.site.register(ProgramApplication, ProgramApplicationAdmin)


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Talent, TalentAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)