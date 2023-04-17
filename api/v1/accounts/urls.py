from django.urls import re_path, path
from api.v1.accounts import views
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)


app_name = "api_v1_accounts"

urlpatterns = [
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	
	re_path(r'^register/',views.register),
	re_path(r'^login/',views.profile_login),
	re_path(r'^chief/$',views.chief_login, name="chief_login"),
]