from django.contrib import admin
from django.urls import path, include 
from home import views 


#Django admin header customization.
admin.site.site_header="Login to Developer Bishesh"
admin.site.site_title="Welcome to Bishesh's Dashboard"
admin.site.index_title="Welcome to this portal "


urlpatterns = [
     path('', views.home, name='home'),
     path('info', views.info, name='info'),
     path('projects', views.projects, name='projects'),
     path('contact', views.contact, name='contact'),
]