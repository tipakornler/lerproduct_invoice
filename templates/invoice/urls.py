from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from invoice.views import invoice_productListView, invoiceListView,invoiceHafeleView, invoicepaid,invoiceAllView, invoiceView, invoicePenkView,invoiceOverAllListView,invoiceAllListView, invoicePenkListView, invoiceHafeleListView



urlpatterns = [
    path('',invoiceAllListView.as_view() ,name='invoice'),
    path('eve/savebl',invoicepaid, name='savebl'),
	path('summary/',invoice_productListView.as_view() ,name='summary'),
	path('eve/',invoiceListView.as_view() ,name='eve'),
	path('hafele/',invoiceHafeleListView.as_view() ,name='hafele'),
	path('penk/',invoicePenkListView.as_view() ,name='penk'),
	path('all/',invoiceOverAllListView.as_view() ,name='all'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    url(r'^(?P<id>\d+)/(?P<tel_number>[-\w]+)/$', views.primary, name='primary'),
    url(r'^(?P<id>\d+)//(7878)/$', views.po, name='po'),
    url(r'^(?P<id>\d+)//(6565)/$', views.delivery, name='delivery'),
    url(r'^(?P<id>\d+)//(6465)/$', views.secondary, name='secondary'),
    path('<int:pk>/', invoiceAllView.as_view(), name='paid-form'),
    path('eve/<int:pk>/', invoiceView.as_view(), name='eve-form'),
    path('hafele/<int:pk>/', invoiceHafeleView.as_view(), name='hafele-form'),
    path('penk/<int:pk>/', invoicePenkView.as_view(), name='penk-form'),

]