from django.contrib import admin
from .models import User, Inventory

# Register your models here.

admin.site.site_header = "Haribookstore Admin"
admin.site.site_title = "HBS | Admin Area"
admin.site.index_title = "Welcome to the HBS Admin Area"

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'user_fname', 'user_lname', 'user_email', 'user_college', 'user_year', 'user_course', 'user_address', 'user_gender', 'user_contactnumber', 'user_birthdate')
    search_fields = ('id', 'user_fname', 'user_lname', 'user_email', 'user_college', 'user_year', 'user_course', 'user_address', 'user_gender', 'user_contactnumber', 'user_birthdate')

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','pro_code', 'pro_name', 'pro_category', 'pro_price', 'pro_quantity', 'pro_sold', 'pro_totalsales')

    search_fields = ('pro_code', 'pro_name', 'pro_category', 'pro_price', 'pro_quantity', 'pro_sold', 'pro_totalsales')

    list_filter = ('pro_category', 'pro_code')

#admin.site.register(User, UserAdmin, Inventory, InventoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Inventory, InventoryAdmin)
