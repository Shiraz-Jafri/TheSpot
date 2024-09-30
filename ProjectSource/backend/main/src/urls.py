
from django.contrib import admin
from django.urls import path, include
from places import views as places_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', places_views.get_places),
]
