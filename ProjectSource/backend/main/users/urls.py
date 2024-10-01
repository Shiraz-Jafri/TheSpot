from django.urls import path
from . import views as user_views

urlpatterns = [
    path('login/', user_views.login),
    path('logout/', user_views.logout),
    path('register', user_views.register),
]
