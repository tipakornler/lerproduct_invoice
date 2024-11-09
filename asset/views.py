from django.shortcuts import render
from .models import	asset
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class asset_ListView(UserPassesTestMixin,ListView):
    template_name = 'asset/asset_listview.html'
    model = asset
    paginate_by = 100
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('asset_name', 'icontains'): a})       
        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('purchase_date','range'): (start_date, end_date)})
        if len(kwargs) >0:
            ptst = asset.objects.filter(**kwargs).order_by("-purchase_date")
        else:
            ptst = asset.objects.filter().order_by("-purchase_date")
        return ptst

    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))
# Create your views here.
