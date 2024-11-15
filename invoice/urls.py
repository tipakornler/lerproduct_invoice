from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from invoice.views import etaxAllView,invoiceBoschView,invoicebshListView,invoicebshView,invoiceBoschListView,invoiceLerSendCompleteView,invoiceLerReceiveView,lerprimary_ListView,invoiceLerReceiveListView,invoiceTecnoView,invoiceTecnoListView,invoiceall_productListView,invoicewithstock_productListView,etaxListView,NoetaxListView,tstprimary_ListView,invoiceLerSendView,invoiceLerSendListView,InvListView,invoiceTekaListView,invoiceBekoListView,invoiceLerListView,invoiceLerView,invoiceBekoView,invoiceTekaView,invoiceTstView,invoice_productListView,invoiceTstListView, invoiceListView,CheckPayment, invoicepaid, invoiceView,invoiceAllView, invoicePenkListView, invoiceHafeleListView,invoiceHafeleView,invoicePenkView,invoiceHflListView,invoiceHflView



urlpatterns = [
    path('',InvListView.as_view() ,name='invoice'),
    path('tst/',invoiceTstListView.as_view() ,name='tst'),
    path('tstlistp/',tstprimary_ListView.as_view() ,name='ptst'),
    path('lerlistp/',lerprimary_ListView.as_view() ,name='pler'),
    path('noetax/',NoetaxListView.as_view() ,name='noetax'),
    path('tst/<int:pk>/', invoiceTstView.as_view(), name='tst-form'),
    url(r'^(?P<id>\d+)/(?P<tel_number>[-\w]+)/(5656)/$', views.primarytst, name='primarytst'),
    url(r'^(?P<id>\d+)/(5454)/$', views.secondarytst, name='secondarytst'),
    path('eve/savebl',invoicepaid, name='savebl'),
	path('summary/',invoice_productListView.as_view() ,name='summary'),
	path('summarywithstock/',invoicewithstock_productListView.as_view() ,name='summarywithstock'),
	path('all/',invoiceall_productListView.as_view() ,name='all'),
    path('summary/addform',views.CheckPayment, name='addform'),
	path('eve/',invoiceListView.as_view() ,name='eve'),
	path('hafele/',invoiceHafeleListView.as_view() ,name='hafele'),
	path('hfl/',invoiceHflListView.as_view() ,name='hfl'),
	path('ler/',invoiceLerListView.as_view() ,name='ler'),
	path('lersend/',invoiceLerSendListView.as_view() ,name='lersend'),
	path('lerreceive/',invoiceLerReceiveListView.as_view() ,name='lerreceive'),
	path('beko/',invoiceBekoListView.as_view() ,name='beko'),
	path('teka/',invoiceTekaListView.as_view() ,name='teka'),
	path('tecno/',invoiceTecnoListView.as_view() ,name='tecno'),
	path('bosch/',invoiceBoschListView.as_view() ,name='bosch'),
	path('lerbsh/',invoicebshListView.as_view() ,name='bsh'),
	path('penk/',invoicePenkListView.as_view() ,name='penk'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    url(r'^(?P<id>\d+)/(?P<tel_number>[-\w]+)/$', views.primary, name='primary'),
    url(r'^(?P<id>\d+)//(6464)/$', views.secondary, name='secondary'),
    url(r'^(?P<id>\d+)//(7878)/$', views.po, name='po'),
    url(r'^(?P<id>\d+)//(8989)/$', views.po_vat, name='po_vat'),
    url(r'^(?P<id>\d+)//(9898)/$', views.lersend_pic, name='lersend_pic'),
    url(r'^(?P<id>\d+)//(6565)/$', views.delivery, name='delivery'),
    url(r'^(?P<id>\d+)//(6868)/$', views.hfl, name='hfl'),
    url(r'^(?P<id>\d+)//(2828)/$', views.cancel, name='cancel'),
    url(r'^(?P<id>\d+)//(8282)/$', views.etaxpaper, name='etaxpaper'),
    url(r'^(?P<id>\d+)//(2424)/$', views.etax_done, name='etax_done'),
    path('eve/<int:pk>/', invoiceView.as_view(), name='eve-form'),
    path('<int:pk>/', invoiceAllView.as_view(), name='paid-form'),
    path('hafele/<int:pk>/', invoiceHafeleView.as_view(), name='hafele-form'),
    path('hfl/<int:pk>/', invoiceHflView.as_view(), name='hfl-form'),
    path('teka/<int:pk>/', invoiceTekaView.as_view(), name='teka-form'),
    path('tecno/<int:pk>/', invoiceTecnoView.as_view(), name='tecno-form'),
    path('bosch/<int:pk>/', invoiceBoschView.as_view(), name='bsh-form'),
    path('lerbsh/<int:pk>/', invoicebshView.as_view(), name='bsh-form'),
    path('beko/<int:pk>/', invoiceBekoView.as_view(), name='beko-form'),
    path('ler/<int:pk>/', invoiceLerView.as_view(), name='ler-form'),
    path('lersend/<int:pk>/', invoiceLerSendView.as_view(), name='lersend-form'),
    path('lersend/6565/<int:pk>/', invoiceLerSendCompleteView.as_view(), name='lersendcomplete-form'),
    path('lerreceive/<int:pk>/', invoiceLerReceiveView.as_view(), name='lerreceive-form'),
    path('penk/<int:pk>/', invoicePenkView.as_view(), name='penk-form'),
    path('etax/',etaxListView.as_view() ,name='etax'),
    path('etax/<int:pk>/',etaxAllView.as_view() ,name='etax_print'),
]