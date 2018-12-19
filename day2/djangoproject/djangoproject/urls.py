from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', views.KickstarterCampaignList.as_view()), 
    path('api/<int:kick_id>/', views.KickstarterCampaignSingle.as_view()), 
]
