from django.contrib import admin
from .models import Event, Gallery, ContactMessage, User, Blog, Talent, Category, ProgramApplication, EquipmentOrder

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
    list_display = ("name", "email", "phone_number", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "phone_number", "message")
    readonly_fields = ("created_at", "name", "email", "phone_number", "message")
    
    def has_add_permission(self, request):
        return False


class ProgramApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "program_interest", "created_at")
    list_filter = ("program_interest", "created_at")
    search_fields = ("full_name", "email", "why_join", "experience")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)


class EquipmentOrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", "full_name", "space_type_display", "services_display", "event_date", "status", "order_date")
    list_filter = ("status", "event_date", "order_date", "space_type", "event_type")
    search_fields = ("full_name", "email", "phone", "event_type")
    readonly_fields = ("order_date", "updated_at", "services_display", "space_type")
    ordering = ("-order_date",)
    
    fieldsets = (
        ("Customer Information", {
            "fields": ("full_name", "email", "phone")
        }),
        ("Event Details", {
            "fields": ("event_type", "event_date", "expected_guests", "space_type")
        }),
        ("Services Requested", {
            "fields": ("services_display",)
        }),
        ("Special Requirements & Notes", {
            "fields": ("special_requirements",)
        }),
        ("Order Status & Timestamps", {
            "fields": ("status", "total_price", "order_date", "updated_at")
        }),
    )
    
    def order_id(self, obj):
        return f"Order #{obj.id}"
    order_id.short_description = "Order ID"
    
    def space_type_display(self, obj):
        """Display the space type with a label"""
        space_type_map = {
            'indoor': '🏢 Indoor Rooms & Halls',
            'outdoor': '🌳 Outdoor Garden Space',
            'both': '🏢🌳 Both (Combined)',
        }
        return space_type_map.get(obj.space_type, obj.space_type)
    space_type_display.short_description = "Space Type"
    
    def services_display(self, obj):
        return obj.get_services_display()
    services_display.short_description = "Services Requested"


admin.site.register(ProgramApplication, ProgramApplicationAdmin)
admin.site.register(EquipmentOrder, EquipmentOrderAdmin)


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Talent, TalentAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)