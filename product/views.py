import json
import urllib.request

from django.shortcuts import render, get_object_or_404,redirect
from .models import allproduct, ContactForm, Category, Brand
from cart.forms import CartAddProductForm
from .forms import contactform
from django.db.models import Q, F
from django.core import mail
from django.utils.html import strip_tags
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView ,DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.conf import settings
from django.contrib import messages



def webredirect(request):
	return render(request, 'menu/redirect.html')


class allproductListView(ListView):
    model = allproduct
    ordering = ['date']
    paginate_by = 9
    def get_queryset(self):
        name = self.request.GET.get('name') 
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')     
        start_price = self.request.GET.get('start_price')
        end_price = self.request.GET.get('end_price')

        kwargs = {}
        if name :
            kwargs.update({'{0}__{1}'.format('productname', 'icontains'): name})

        if category :
            kwargs.update({'{0}'.format('category__slug'): category})

        if brand :
            kwargs.update({'{0}'.format('brand'): brand})

        if start_price and end_price :
            kwargs.update({'{0}__{1}'.format('productprice', 'range'): [start_price,end_price]})

        if len(kwargs) >0:
            products = allproduct.objects.filter(Q(**kwargs),
                Q(promotiontime__gte = datetime.date.today()) |
                Q(promotiontime__isnull=True),status=True).order_by('productprice','promotion')
        else:
            products = allproduct.objects.filter(Q(promotiontime__gte = datetime.date.today()) |
                Q(promotiontime__isnull=True),status=True).order_by('-promotion','-promotiontime','?')
        return products
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(allproductListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['cart_product_form'] = CartAddProductForm()
        return context


def productdetail(request, id, productid):
    detail = get_object_or_404(allproduct, id=id)
    cart_product_form = CartAddProductForm()
    context = {
            'detail':detail,
            'cart_product_form':cart_product_form
    }
    return render(request, 'detail.html', context)



def contact(request):
	return render(request, 'menu/contact.html')

def addcontactform(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        tel = request.POST.get('tel')
        contact_message = request.POST.get('contact_message')

        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                form.save()
                subject = 'คำถาม'
                html_message = contact_name + '<br>' +  contact_email + '<br>'+ tel + '<br>'+ contact_message
                plain_message = strip_tags(html_message)
                from_email = 'Eve-Product.com <lercorpt@gmail.com>'
                to = 'tipakorn.ler@gmail.com'

                mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
            else:
                messages.error(request, 'การยืนยันตัวตนผิดพลาด กรุณาลองใหม่อีกครั้ง (Invalid reCAPTCHA)')
                return redirect('contact')
    return render(request, 'menu/receiveform.html', {'form': contactform})

def insure(request):
	return render(request, 'menu/insure.html')

def insure_eve(request):
	return render(request, 'menu/insure_eve.html')

def about(request):
	return render(request, 'menu/about.html')

def trans(request):
    return render(request, 'menu/trans.html')

def test(request):
    return render(request, 'test.html')