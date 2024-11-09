from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from newproduct.views import NewproductListView,NewproductView,createnewAllView


urlpatterns = [
    path('',NewproductListView.as_view() ,name='new'),
    path('<int:pk>', NewproductView.as_view(), name='status'),
    path('addproduct',createnewAllView.as_view() ,name='addproduct'),
    path('done/', views.done,name='done'),
]