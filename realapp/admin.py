from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,atendance,task


class CustomUserAdmin(admin.ModelAdmin):
    # Specify which fields to display in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    
   

    # If you want to make any fields read-only in the admin
    readonly_fields = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)

class attend(admin.ModelAdmin):
    list_display=('user','date',)

admin.site.register(atendance,attend)
class taskadmin(admin.ModelAdmin):
    list_display=('user','title',)

admin.site.register(task,taskadmin)


