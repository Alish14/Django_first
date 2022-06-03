from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

class accountAdmin(UserAdmin):
    list_display=('email','username','date_joined','last_login','is_admin','is_staff')
    search_feild=('email','username')
    readonly_feilds=('id','date_joined','last_login')
    filter_horizontal=()
    list_filter=()
admin.site.register(Account,accountAdmin)


# Register your models here.
