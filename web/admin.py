from django.contrib import admin

from web.models import About, Enquiry, Gallery, Services

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'photo', 'is_deleted')
admin.site.register(About,AboutAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'photo', 'is_deleted')
admin.site.register(Services,ServiceAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo')
admin.site.register(Gallery,GalleryAdmin)


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email')
    search_fields = ('name', 'phone')
admin.site.register(Enquiry,EnquiryAdmin)
