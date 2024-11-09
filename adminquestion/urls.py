from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from adminquestion.views import QuestionListView


urlpatterns = [
	path('adminquestion/',QuestionListView.as_view() ,name='adminquestion'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),

]