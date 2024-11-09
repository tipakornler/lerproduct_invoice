from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    path('create/addpayment',views.addpayment ,name='addpayment'),
    path('payment/addpayment',views.addpayment ,name='addpayment'),
    path('create/paylater',views.paylater ,name='paylater'),
    path('payment/',views.showpayment ,name='payment'),
    path('paymentmade/',views.paymentmade, name='paymentmade')

]