from django.contrib import admin

from accounts.models import ChiefProfile, Profile 

class ChiefProfileAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'username', 'password')
    exclude = ('auto_id', 'creator', 'updater', 'is_deleted', 'password', 'user')
    search_fields = ('user', )

admin.site.register(ChiefProfile, ChiefProfileAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_added', 'name', 'phone', 'email',
                     'is_verified', 'password', 'gender', 'dob')
    ordering = ('-date_added',)
    search_fields = ('phone', 'pk', 'user__username', 'name')
    
admin.site.register(Profile,ProfileAdmin)

