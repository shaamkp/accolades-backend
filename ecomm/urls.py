from django.contrib import admin
from django.views.static import serve
from django.urls import path, include, re_path
from django.conf import settings as SETTINGS


admin.site.site_header = "Accolades Admin"
admin.site.site_title = "Accolades Admin"
admin.site.index_title = "Welcome to Accolades Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/accounts/', include('api.v1.accounts.urls', namespace="api_v1_accounts")),
    path('api/v1/web/', include('api.v1.web.urls', namespace="api_v1_web")),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': SETTINGS.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': SETTINGS.STATIC_FILE_ROOT}),

]
