from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from problem.views import IssueListView,IssueView


urlpatterns = [
    path('',IssueListView.as_view() ,name='issue'),
    path('<int:pk>', IssueView.as_view(), name='status'),
]