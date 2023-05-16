from django.contrib import admin
from .models import Flat
from .models import Owner
from .models import Complaint


class OwnershipInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', )
    readonly_fields = ('created_at', )
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town', )
    list_editable = ('new_building', )
    list_filter = ('new_building', 'rooms_number', 'has_balcony', )
    raw_id_fields = ('liked_by',)

    inlines = [
        OwnershipInline,
    ]


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number',
                    'pure_phone_number',)
    raw_id_fields = ('flats',)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text')
    list_filter = ('user', )
    raw_id_fields = ('flat',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
