from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from transport.views import transportlistView



urlpatterns = [
    path('',transportlistView.as_view() ,name='trans'),
]