from django.contrib import admin
from .models import Flat
from .models import Complaint
from .models import UserProfile
from .models import Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner', 'owner_pure_phone', )
    readonly_fields = ('created_at', )
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owner_pure_phone', )
    list_editable = ('new_building', )
    list_filter = ('new_building', 'rooms_number', 'has_balcony', )
    raw_id_fields = ('liked_by',)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text')
    list_filter = ('user', )
    raw_id_fields = ('flat',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    raw_id_fields = ('user',)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'owners_phonenumber', \
                    'owner_pure_phone',)
    raw_id_fields = ('flats',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Owner, OwnerAdmin)
