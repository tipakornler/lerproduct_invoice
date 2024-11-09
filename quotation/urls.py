from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from quotation.views import QuoListView



urlpatterns = [
    path('',QuoListView.as_view() ,name='quotation'),
    url(r'^(?P<id>\d+)//(7878)/$', views.quo_vat, name='quo_vat'),
]