from django.shortcuts import render
from django.views.generic import ListView, DetailView ,DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import	trans
from django.db.models import Q, F, FloatField
from django.db.models import Sum, Count

class transportlistView(UserPassesTestMixin,ListView):
    template_name = 'trans/list_trans.html'
    model = trans
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        kwargs = {}
        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('send_date','range'): (start_date, end_date)})
        if len(kwargs) >0:
            trnasport = trans.objects.filter(**kwargs).order_by("-send_date")
        else:
            trnasport = trans.objects.filter().order_by("-send_date")
        return trnasport
    def get_context_data(self, **kwargs):
        context = super(transportlistView, self).get_context_data(**kwargs)
        # Call the base implementation first to get a context
        mile = ((F('mile_stop')-(F('mile_start'))))
        total_mile = self.get_queryset().filter().aggregate(total=(Sum(mile)))['total']
        toll_fee = ((F('toll_fee')))
        total_toll_fee = self.get_queryset().filter().aggregate(total=(Sum(toll_fee)))['total']

        cost = ((F('mile_stop')-(F('mile_start')))*3) + (F('outsouce_trans')) + (F('other_cost')) + (F('toll_fee')) + (F('fuel_cost'))
        total_cost = self.get_queryset().filter().aggregate(total=(Sum(cost)))['total']
        receive = (F('receive'))+ (F('other_receive'))
        total_receive = self.get_queryset().filter().aggregate(total=(Sum(receive)))['total']
        fuel = (F('fuel_cost'))
        total_fuel = self.get_queryset().filter().aggregate(total=(Sum(fuel)))['total']
        outsource_cost = (F('outsouce_trans'))
        total_outsource_cost_cost = self.get_queryset().filter().aggregate(total=(Sum(outsource_cost)))['total']
        # total_sell_price = 0 if not total_sell_price else total_sell_price
        total_toll_fee = 0 if not total_toll_fee else total_toll_fee  
        total_fuel = 0 if not total_fuel else total_fuel  
        total_cost = 0 if not total_cost else total_cost
        total_receive = 0 if not total_receive else total_receive
        total_outsource_cost_cost = 0 if not total_outsource_cost_cost else total_outsource_cost_cost
        total_mile = 0 if not total_mile else total_mile
        summary = {
            'total_cost': total_cost,
            'total_receive':total_receive,
            'total_fuel':total_fuel,
            'total_outsource_cost_cost':total_outsource_cost_cost,
            'total_mile':total_mile,
            'total_toll_fee':total_toll_fee,
        }
        context['summary'] = summary
        return context
    
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))
    
# Create your views here.
