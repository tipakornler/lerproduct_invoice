from django.shortcuts import render
from django.views.generic import ListView, DetailView ,DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q, F, FloatField
from .models import	issue

# Create your views here.



class IssueListView(UserPassesTestMixin,ListView):
    template_name = 'issue/pending_issue.html'
    model = issue
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('order_number__order_number', 'icontains'): a})
        
        if start_date and end_date :
            kwargs.update({'{0}__{1}__{2}'.format('created','date', 'range'): (start_date, end_date)})

        if len(kwargs) >0:
            hh = issue.objects.filter(**kwargs).order_by("status",'created')
        else:
            hh = issue.objects.filter().order_by("status",'created')
        return hh
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))

class IssueView(UserPassesTestMixin,UpdateView):
    model = issue
    fields = ['status','onprocess','topic','description']
    template_name = 'issue/issue_detail.html'
    success_url = '/issue/'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))