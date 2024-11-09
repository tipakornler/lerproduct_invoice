from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from product import views
from django.contrib.auth import views as auth_views
from product.views import allproductListView

app_name = 'lerproduct'

urlpatterns = [
    path('',allproductListView.as_view() ,name='product_list'),
    path('asset/', include('asset.urls')),
    path('admin/', admin.site.urls),
    path('invoice/', include('invoice.urls')),
    path('inv/', include('inventory.urls')),
    path('new/', include('newproduct.urls')),
    path('reqinv/', include('reqinv.urls')),
    path('issue/', include('problem.urls')),
    path('qa/', include('adminquestion.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.allproductListView, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<productid>[-\w]+)/$', views.productdetail, name='productdetail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

