from django.conf.urls import url
from . import views
from django.urls import path
from .views import get_promo_info,PromoListView


urlpatterns = [
    path('' ,PromoListView.as_view(), name='promo'),
    path('api/<str:code_name>',get_promo_info ,name='promocode-api'),
]