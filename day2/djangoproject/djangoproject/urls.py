from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/kickstarter/<int:id>', views.get_kickstarter), 
    path('api/kickstarter/all', views.get_all_kickstarter), 
    
]
