
from django.contrib import admin
from django.urls import path, include
from places import views as places_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('spots/', places_views.get_spots, name='spots-page'),
    path('spot/', places_views.get_a_spot, name='spot-page'),
    path('users/', include('users.urls')),
]