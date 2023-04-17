from django.urls import re_path, path
from api.v1.web import views

app_name = "api_v1_web"

urlpatterns = [
	re_path(r'^abouts/$',views.abouts),
	re_path(r'^add-abouts/$',views.add_abouts),
	re_path(r'^edit-abouts/(?P<pk>.*)/$',views.edit_abouts),
	re_path(r'^delete-abouts/(?P<pk>.*)/$',views.delete_abouts),

	re_path(r'^services/$',views.services),
	re_path(r'^add-services/$',views.add_services),
	re_path(r'^edit-services/(?P<pk>.*)/$',views.edit_services),
	re_path(r'^delete-services/(?P<pk>.*)/$',views.delete_services),


	re_path(r'^galleries/$',views.galleries),
	re_path(r'^add-galleries/$',views.add_galleries),
	re_path(r'^edit-galleries/(?P<pk>.*)/$',views.edit_galleries),
	re_path(r'^delete_galleries/(?P<pk>.*)/$',views.delete_galleries),
	
	re_path(r'^add-enquiries/$',views.add_enquiries),

]