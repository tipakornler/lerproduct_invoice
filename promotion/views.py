from django.shortcuts import render
from django.views.generic import ListView, DetailView ,DeleteView, UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q, F, FloatField
from .models import	listpromo
from django.urls import reverse_lazy

# Create your views here.



class PromotionListView(UserPassesTestMixin,ListView):
    template_name = 'promotion/promotion_list.html'
    model = listpromo
    ordering = ['date']
    paginate_by = 50
    def get_queryset(self):
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        c = self.request.GET.get('c')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('product_name', 'icontains'): a})

        if b :
            kwargs.update({'{0}'.format('status_create'): b})

        if c :
            kwargs.update({'{0}'.format('status_shopee'): c})


        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('updated','range'): (start_date, end_date)})

        if len(kwargs) >0:
            hh = listpromo.objects.filter(**kwargs).order_by('-created',"status_mainweb")
        else:
            hh = listpromo.objects.filter().order_by('-created',"status_mainweb")
        return hh
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))

class NewproductView(UserPassesTestMixin,UpdateView):
    model = new
    fields = ['status_create','status_shopee','status_lazada','status_nocnoc','status_tiktok','status_mainweb','vdo','low_quality','comment','youtube_link']
    template_name = 'newproduct/newproduct_detail.html'
    success_url = '/new/'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))
    

class createnewAllView(CreateView):
    model = new
    form_class = newpForm
    template_name = 'newproduct/input.html'
    success_url = reverse_lazy('done')
    def test_func(self):
        return self.request


def done(request) :
    return render(request, 'newproduct/receiveform.html')