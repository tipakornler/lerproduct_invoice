from django.conf.urls import url
from . import views
from django.urls import path
from .views import asset_ListView


urlpatterns = [
    path('' ,asset_ListView.as_view(), name='asset'),
]