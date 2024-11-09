from datetime import date
from socket import TCP_NODELAY
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q, F, FloatField
from .models import	quotation,quotation_product
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.db.models import Sum, Count
from django.views.generic import ListView, DetailView ,DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math
from django.db.models import IntegerField
from django.db.models.functions import Cast


def number_format(num, places=0):
    return '{:20,.2f}'.format(num)
# fork by http://justmindthought.blogspot.com/2012/12/code-php.html
def ThaiBahtConversion(amount_number):
    amount_number = number_format(amount_number, 2).replace(" ","")
    pt = amount_number.find(".")
    number,fraction = "",""
    amount_number1 = amount_number.split('.')
    if (pt == False):
        number = amount_number
    else:
        amount_number = amount_number.split('.')
        number = amount_number[0]
        fraction = int(amount_number1[1]) 
    ret = ""
    number=eval(number.replace(",",""))
    baht = ReadNumber(number)
    if (baht != ""):
        ret += baht + "บาท"
    satang = ReadNumber(fraction)
    if (satang != ""):
        ret += satang + "สตางค์"
    else:
        ret += "ถ้วน"
    return ret
 
#อ่านจำนวนตัวเลขภาษาไทย
def ReadNumber(number):
    """อ่านจำนวนตัวเลขภาษาไทย รับค่าเป็น ''float'' คืนค่าเป็น  ''str''"""
    position_call = ["แสน", "หมื่น", "พัน", "ร้อย", "สิบ", ""]
    number_call = ["", "หนึ่ง", "สอง", "สาม","สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    number = number
    ret = ""
    if (number == 0): return ret
    if (number > 1000000):
        ret += ReadNumber(int(number / 1000000)) + "ล้าน"
        number = int(math.fmod(number, 1000000))
    divider = 100000
    pos = 0
    while(number > 0):
        d=int(number/divider)
        if (divider == 10) and (d == 2):
            ret += "ยี่"
        elif (divider == 10) and (d == 1):
            ret += ""
        elif ((divider == 1) and (d == 1) and (ret != "")):
            ret += "เอ็ด"
        else:
            ret += number_call[d]
        if(d):
            ret += position_call[pos]
        else:
            ret += ""
        number=number % divider
        divider=divider / 10
        pos += 1
    return ret

class QuoListView(UserPassesTestMixin,ListView):
    template_name = 'quotation/list.html'
    model = quotation_product
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        q = self.request.GET.get('q')

        kwargs = {}
        if q :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): q})

        if len(kwargs) >0:
            listall = quotation_product.objects.filter(**kwargs).order_by("-created")
        else:
            listall = quotation_product.objects.filter().order_by("-created")
        return listall
    def get_context_data(self, **kwargs):
        context = super(QuoListView, self).get_context_data(**kwargs)
        total_a = self.get_queryset().aggregate(a=Sum(F('sell_price')*F('qty')))['a']
        summary = {
            'total_a':total_a,
        }
        # Add in the publisher
        context['summary'] = summary
        return context
    def test_func(self):
        return self.request.user.username.startswith('admin')

def quo_vat(request, id):
    detail = get_object_or_404(quotation, id=id)
    total_cost = detail.quos.aggregate(result=Sum((F('sell_price')*F('qty')), output_field=FloatField()))['result']
    baht = ThaiBahtConversion(total_cost)
    context = {
            'detail':detail,
            'total_cost':total_cost,
            'baht':baht,
    }
    return render(request,'quotation/detail_quo_vat.html',context)






    







    

    


