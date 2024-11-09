from django.conf.urls import url
from . import views
from django.urls import path
from .views import inListView,outListView,invsummaryListView


urlpatterns = [
    path('' ,invsummaryListView.as_view(), name='summary'),
    path('in' ,inListView.as_view(), name='in'),
    path('out' ,outListView.as_view(), name='out'),
]