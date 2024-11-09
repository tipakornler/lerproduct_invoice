from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from reqinv.views import reqinvAllView



urlpatterns = [
    path('',reqinvAllView.as_view() ,name='reqinv'),
    path('success/', views.success,name='success'),
]