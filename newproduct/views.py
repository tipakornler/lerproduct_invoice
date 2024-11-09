from django.shortcuts import render
from django.views.generic import ListView, DetailView ,DeleteView, UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q, F, FloatField
from .models import	new
from newproduct.forms import newpForm
from django.urls import reverse_lazy

# Create your views here.



class NewproductListView(UserPassesTestMixin,ListView):
    template_name = 'newproduct/pending_newproduct.html'
    model = new
    ordering = ['date']
    paginate_by = 50
    def get_queryset(self):
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        c = self.request.GET.get('c')
        d = self.request.GET.get('d')
        e = self.request.GET.get('e')
        f = self.request.GET.get('f')
        g = self.request.GET.get('g')
        h = self.request.GET.get('h')
        i = self.request.GET.get('i')
        j = self.request.GET.get('j')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('product_name', 'icontains'): a})

        if b :
            kwargs.update({'{0}'.format('status_create'): b})

        if c :
            kwargs.update({'{0}'.format('status_shopee'): c})

        if d :
            kwargs.update({'{0}'.format('status_lazada'): d})

        if e :
            kwargs.update({'{0}'.format('status_nocnoc'): e})

        if f :
            kwargs.update({'{0}'.format('status_tiktok'): f})

        if g :
            kwargs.update({'{0}'.format('status_mainweb'): g})

        if h :
            kwargs.update({'{0}'.format('vdo'): h})

        if i :
            kwargs.update({'{0}'.format('low_quality'): i})

        if j :
            kwargs.update({'{0}__{1}'.format('youtube_link', 'icontains'): j})


        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('updated','range'): (start_date, end_date)})

        if len(kwargs) >0:
            hh = new.objects.filter(**kwargs).order_by('-created',"status_mainweb")
        else:
            hh = new.objects.filter().order_by('-created',"status_mainweb")
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