from django.urls import re_path
from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.v1.general import views
app_name = "api_v1_general"

urlpatterns = [
    re_path(r'^get_details/$', views.get_details),

    url('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]