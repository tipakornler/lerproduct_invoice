from django.shortcuts import render
from .models import	InventoryIn, InventoryOut
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView ,DeleteView, UpdateView, CreateView
from django.db.models import Sum, Count
from django.db.models import Q, F, FloatField
# Create your views here.


class invsummaryListView(UserPassesTestMixin,ListView):
    template_name = 'inv/inv_summary.html'
    model = InventoryOut
    paginate_by = 50
    def get_queryset(self):
        a = self.request.GET.get('a')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('order_id__product', 'icontains'): a})
    
        if start_date and end_date :
            kwargs.update({'{0}__{1}__{2}'.format('created','date', 'range'): (start_date, end_date)})

        if len(kwargs) >0:
            stock = InventoryOut.objects.filter(**kwargs).order_by("-created")
        else:
            stock = InventoryOut.objects.filter().order_by("-created")
        return stock
    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super(invsummaryListView, self).get_context_data(**kwargs)
        # # total_sell_price = self.get_queryset().aggregate(a=Sum(F('sell_price')*F('qty')))['a']
        # total_qty_in = self.get_queryset().aggregate(a=Sum(F('.qty')))['a']
        # total_qty_out = self.get_queryset().aggregate(a=Sum(F('qty')))['a']
        stock = {
            # 'total_qty_in':total_qty_in,
            # 'total_qty_out':total_qty_out
            # 'vat_pay':((total_sell_price-total_cost)/total_vat)-(total_sell_price-total_cost),
        }
        # Add in the publisher
        context['stock'] = stock
        return context
    def test_func(self):
        return self.request.user.username.startswith('admin')


class inListView(UserPassesTestMixin,ListView):
    template_name = 'inv/list_in.html'
    model = InventoryIn
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('product__productname', 'icontains'): a})
        
        if start_date and end_date :
            kwargs.update({'{0}__{1}__{2}'.format('created','date', 'range'): (start_date, end_date)})

        if len(kwargs) >0:
            search = InventoryIn.objects.filter(**kwargs).order_by('created')
        else:
            search = InventoryIn.objects.filter().order_by('created')
        return search
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))
    
class outListView(UserPassesTestMixin,ListView):
    template_name = 'inv/list_out.html'
    model = InventoryOut
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('allproduct__product', 'icontains'): a})
        
        if start_date and end_date :
            kwargs.update({'{0}__{1}__{2}'.format('created','date', 'range'): (start_date, end_date)})

        if len(kwargs) >0:
            search = InventoryOut.objects.filter(**kwargs).order_by('created')
        else:
            search = InventoryOut.objects.filter().order_by('created')
        return search
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))