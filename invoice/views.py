from datetime import date
from socket import TCP_NODELAY
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q, F, FloatField
from .models import	invoice, invoice_product
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.db.models import Sum, Count
from django.views.generic import ListView, DetailView ,DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math
from django.views.generic.edit import UpdateView
from .forms import CheckPaymentForm
from django.db.models import IntegerField
from django.db.models.functions import Cast

def invoicepaid(request):
    page = request.POST['page']
 
    bl_list = request.POST.getlist('bill')# list of BL id
    payments = invoice.objects.filter(id__in = bl_list )
    payments.update(billable=True)

    note_list = request.POST.getlist('note')
    noteadd = request.POST.get('noteadd')
    print(note_list)
    listnote = invoice_product.objects.filter(id__in = note_list)

    listnote.update(evenote=noteadd)

    
    return HttpResponseRedirect(reverse_lazy('eve') + "?page=" + page)

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

class tstprimary_ListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/detail_primary_month_tst.html'
    model = invoice
    paginate_by = 100
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        kwargs = {}
        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('name__invoice_date','range'): (start_date, end_date)})
        if len(kwargs) >0:
            ptst = invoice_product.objects.filter(**kwargs,name__invoice=True,brand=13,created__year__gt="2021",created__month__gt="0").order_by("-created")
        else:
            ptst = invoice_product.objects.filter(name__invoice=True,brand=13,created__year__gt="2022",created__month__gt="0").order_by("-created")
        return ptst

    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))
    
class lerprimary_ListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/detail_primary_month_ler.html'
    model = invoice
    paginate_by = 1000
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        kwargs = {}
        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('name__invoice_date','range'): (start_date, end_date)})
        if len(kwargs) >0:
            pler = invoice_product.objects.filter(**kwargs,name__invoice=True,created__year__gt="2021",created__month__gt="0").order_by("-created")
        else:
            pler = invoice_product.objects.filter(name__invoice=True,created__year__gt="2022",created__month__gt="0").order_by("-created")
        return pler

    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))


class invoiceTstListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/list_tst.html'
    model = invoice_product
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        c = self.request.GET.get('c')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        d = self.request.GET.get('d')
        e = self.request.GET.get('e')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): a})
        if b :
            kwargs.update({'{0}'.format('name__print_tst'): b})
        if c :
            kwargs.update({'{0}__{1}'.format('name__address', 'icontains'): c})
        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('name__invoice_date','range'): (start_date, end_date)})
        if d and e :
            kwargs.update({'{0}__{1}'.format('name__updated','range'): (d, e)})
        if len(kwargs) >0:
            tst = invoice_product.objects.filter(**kwargs,name__invoice=True,brand=13,created__year__gt="2021",created__month__gt="0").order_by("-created")
        else:
            tst = invoice_product.objects.filter(name__invoice=True,brand=13,created__year__gt="2022",created__month__gt="0").order_by("-created")
        return tst
    def get_context_data(self, **kwargs):
        context = super(invoiceTstListView, self).get_context_data(**kwargs)
        total_a = self.get_queryset().aggregate(a=Sum(F('sell_price')*F('qty')))['a']
        summary = {
            'total_a':total_a,
        }
        # Add in the publisher
        context['summary'] = summary
        return context
    def test_func(self):
        return self.request.user.username.startswith('admin')

def primarytst(request, id, tel_number):
    detail = get_object_or_404(invoice, id=id)
    total_price = detail.invoices.aggregate(result=Sum(F('received')*F('qty')*0.92))['result']
    baht = ThaiBahtConversion(total_price)
    context = {
            'detail':detail,
            'total_price':total_price,
            'baht':baht,
    }
    return render(request,'invoice/detail_primary_tst.html',context)


def secondarytst(request, id):
    detail = get_object_or_404(invoice, id=id)
    total_price = detail.invoices.aggregate(result=Sum(F('received')*F('qty')*0.92))['result']
    baht = ThaiBahtConversion(total_price)
    context = {
            'detail':detail,
            'total_price':total_price,
            'baht':baht,
    }
    return render(request,'invoice/detail_secondary_tst.html',context)

class invoiceTstView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['print_tst']
    template_name = 'invoice/tst_paid.html'
    success_url = '/invoice/tst'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))

class InvListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/list.html'
    model = invoice_product
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        q = self.request.GET.get('q')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        c = self.request.GET.get('c')
        d = self.request.GET.get('d')
        e = self.request.GET.get('e')
        g = self.request.GET.get('g')
        h = self.request.GET.get('h')
        i = self.request.GET.get('i')
        kwargs = {}
        if q :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): q})
        if a :
            kwargs.update({'{0}__{1}'.format('name__tel_number', 'icontains'): a})
        if b :
            kwargs.update({'{0}'.format('name__paid'): b})
        if c :
            kwargs.update({'{0}__{1}'.format('name__address', 'icontains'): c})
        if d :
            kwargs.update({'{0}__{1}'.format('name__count_invoice_number', 'icontains'): d})
        if e :
            kwargs.update({'{0}'.format('name__cancel_inv'): e})
        if g :
            kwargs.update({'{0}__{1}'.format('brand__brand_name', 'icontains'): g})

        if h and i :
            kwargs.update({'{0}__{1}'.format('name__updated','range'): (h, i)})

        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('name__invoice_date','range'): (start_date, end_date)})
        if len(kwargs) >0:
            listall = invoice_product.objects.filter(**kwargs,name__invoice=True).order_by("-created")
        else:
            listall = invoice_product.objects.filter(name__invoice=True).order_by("-created")
        return listall
    def get_context_data(self, **kwargs):
        context = super(InvListView, self).get_context_data(**kwargs)
        total_a = self.get_queryset().aggregate(a=Sum(F('sell_price')*F('qty')))['a']
        summary = {
            'total_a':total_a,
        }
        # Add in the publisher
        context['summary'] = summary
        return context
    def test_func(self):
        return self.request.user.username.startswith('admin')
    # if request.GET.get('q'):
    #     listall = invoice.objects.filter(Q(name__icontains=query) | Q(invoice_eve__icontains=query) | Q(address__icontains=query),invoice=True).order_by("billable","-created")
    # page = request.GET.get('page')
    # paginator = Paginator(listall, 20)

    # try:
    #     listall = paginator.page(page)
    # except PageNotAnInteger:
    #     listall = paginator.page(1)
    # except EmptyPage:
    #     listall = paginator.page(paginator.num_pages)
    # context = {
    #     'listall': listall
    # }
    # # Define parameter
    # return render(request,'invoice/list.html', context)
# Create your views here.

def primary(request, id, tel_number):
    detail = get_object_or_404(invoice, id=id)
    total_price = detail.invoices.aggregate(result=Sum(F('sell_price')*F('qty')))['result']
    baht = ThaiBahtConversion(total_price)
    context = {
            'detail':detail,
            'total_price':total_price,
            'baht':baht,
    }
    return render(request,'invoice/detail_primary.html',context)


def secondary(request, id):
    detail = get_object_or_404(invoice, id=id)
    total_price = detail.invoices.aggregate(result=Sum(F('sell_price')*F('qty')))['result']
    baht = ThaiBahtConversion(total_price)
    context = {
            'detail':detail,
            'total_price':total_price,
            'baht':baht,
    }

    return render(request,'invoice/detail_secondary.html',context)


def cancel(request, id):
    detail = get_object_or_404(invoice, id=id)
    total_price = detail.invoices.aggregate(result=Sum(F('sell_price')*F('qty')))['result']
    baht = ThaiBahtConversion(total_price)
    context = {
            'detail':detail,
            'total_price':total_price,
            'baht':baht,
    }
    return render(request,'invoice/cancel_form.html',context)

def delivery(request, id):
    detail = get_object_or_404(invoice, id=id)
    total_price = detail.invoices.aggregate(result=Sum(F('sell_price')*F('qty')))['result']
    baht = ThaiBahtConversion(total_price)
    context = {
            'detail':detail,
            'total_price':total_price,
            'baht':baht,
    }

    return render(request,'invoice/detail_delivery.html',context)


def hfl(request, id):
    detail = get_object_or_404(invoice, id=id)
    total_price = detail.invoices.aggregate(result=Sum(F('sell_price')*F('qty')))['result']
    baht = ThaiBahtConversion(total_price)
    context = {
            'detail':detail,
            'total_price':total_price,
            'baht':baht,
    }

    return render(request,'invoice/detail_delivery_hfl.html',context)


def po(request, id):
    detail = get_object_or_404(invoice, id=id)
    total_cost = detail.invoices.aggregate(result=Sum((F('real_price')*(100.00-F('gp'))/100.00)*F('qty'), output_field=FloatField()))['result']
    baht = ThaiBahtConversion(total_cost)
    context = {
            'detail':detail,
            'total_cost':total_cost,
            'baht':baht,
    }
    return render(request,'invoice/detail_po.html',context)

def po_vat(request, id):
    detail = get_object_or_404(invoice, id=id)
    total_cost = detail.invoices.aggregate(result=Sum((F('real_price')*(100.00-F('gp'))/100.00)*F('qty'), output_field=FloatField()))['result']
    baht = ThaiBahtConversion(total_cost)
    context = {
            'detail':detail,
            'total_cost':total_cost,
            'baht':baht,
    }
    return render(request,'invoice/detail_po_vat.html',context)




class invoice_productListView(UserPassesTestMixin,ListView):
    model = invoice_product
    ordering = ['date']
    paginate_by = 50
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        c = self.request.GET.get('c')
        d = self.request.GET.get('d')
        e = self.request.GET.get('e')
        f = self.request.GET.get('f')
        s_date = self.request.GET.get('s_date')
        e_date = self.request.GET.get('e_date')
        cs_date = self.request.GET.get('cs_date')
        ce_date = self.request.GET.get('ce_date')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): a})

        if b :
            kwargs.update({'{0}__{1}'.format('brand__brand_name', 'icontains'): b})

        if c :
            kwargs.update({'{0}__{1}'.format('platform', 'icontains'): c})

        if d :
            kwargs.update({'{0}'.format('name__invoice'): d})
        
        if e :
            kwargs.update({'{0}'.format('paymentmade'): e})

        if f :
            kwargs.update({'{0}'.format('money_collect'): f})

        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('name__invoice_date','range'): (start_date, end_date)})

        if s_date and e_date :
            kwargs.update({'{0}__{1}'.format('payment_date','range'): (s_date, e_date)})

        if cs_date and ce_date :
            kwargs.update({'{0}__{1}'.format('collect_date','range'): (cs_date, ce_date)})

        if len(kwargs) >0:
            summary = invoice_product.objects.filter(**kwargs,name__invoice_date__year__gt="2021",name__invoice_date__month__gt="0",name__cancel_inv=False,name__invoice=True).order_by("-created")
        else:

            summary = invoice_product.objects.filter(name__invoice_date__year__gt="2021",name__invoice_date__month__gt="0",name__cancel_inv=False,name__invoice=True).order_by("-created")
        return summary
    def get_context_data(self, **kwargs):
        context = super(invoice_productListView, self).get_context_data(**kwargs)
        total_received = self.get_queryset().aggregate(a=Sum(F('received')*F('qty')))['a']
        total_order = self.get_queryset().aggregate(a=Count('name__order_number',distinct=True))['a']
        total_bill = self.get_queryset().aggregate(a=Sum(F('sell_price')*F('qty')))['a']
        total_tst = self.get_queryset().filter(brand=13).aggregate(tst=Sum(F('received')*F('qty')*0.92))['tst']
        total_received_eve = self.get_queryset().filter(brand=1).aggregate(a=Sum(F('received')*F('qty')))['a']
        total_received_hafele = self.get_queryset().filter(Q(brand=2) | Q(brand = 13)).aggregate(a=Sum(F('received')*F('qty')))['a']
        total_received_mex = self.get_queryset().filter(Q(brand=3) | Q(brand = 9)).aggregate(a=Sum(F('received')*F('qty')))['a']
        total_received_other = self.get_queryset().filter(Q(brand=4) | Q(brand = 5) | Q(brand = 6) | Q(brand = 7) | Q(brand = 8) | Q(brand = 10) | Q(brand = 11)| Q(brand = 12) | Q(brand = 14) | Q(brand = 15)| Q(brand = 16)| Q(brand = 17)).aggregate(a=Sum(F('received')*F('qty')))['a']
        total_received_trasport = self.get_queryset().filter(Q(name__ler_pickup=True)).aggregate(a=Sum(F('real_price')*F('qty')*F('gp')/100))['a']
        cost = (((('100'-F('gp'))*F('real_price')))*F('qty'))
        total_cost = self.get_queryset().aggregate(total=Sum(cost)/100)['total']
        total_received = 0 if not total_received else total_received
        # total_sell_price = 0 if not total_sell_price else total_sell_price
        total_cost = 0 if not total_cost else total_cost
        total_vat = Decimal('1.07')

        summary = {
            'total_received': total_received,
            'total_received_mex':total_received_mex,
            'total_tst':total_tst,
            'total_received_other':total_received_other,
            'total_received_eve':total_received_eve,
            'total_received_hafele':total_received_hafele,
            'profit':total_received - total_cost,
            'percent_profit':(int(1)-(int(1)-(total_received - total_cost)/total_cost))*100 if total_cost != 0 else 0,
            'need_pay':total_cost,
            'total_bill':total_bill,
            'total_order':total_order,
            'total_received_trasport':total_received_trasport,
            # 'vat_pay':((total_sell_price-total_cost)/total_vat)-(total_sell_price-total_cost),
        }
        # Add in the publisher
        context['summary'] = summary
        return context
    def test_func(self):
        return self.request.user.username.startswith('admin')

class invoiceListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/invoice_list.html'
    model = invoice
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): a})
        
        if start_date and end_date :
            kwargs.update({'{0}__{1}__{2}'.format('created','date', 'range'): (start_date, end_date)})

        if len(kwargs) >0:
            eve = invoice_product.objects.filter(**kwargs,name__cancel_inv=False,brand=1).order_by('name__invoice_eve','-created')
        else:
            eve = invoice_product.objects.filter(brand=1,name__cancel_inv=False).order_by('name__invoice_eve','-created')
        return eve
    def test_func(self):
        return self.request.user.username.startswith(tuple(['eve','admin']))





class invoiceHafeleListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/invoice_list_hafele.html'
    model = invoice
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        hafele = self.request.GET.get('hafele')
        kwargs = {}
        if hafele :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): hafele})
        
        if start_date and end_date :
            kwargs.update({'{0}__{1}__{2}'.format('created','date', 'range'): (start_date, end_date)})

        if len(kwargs) >0:
            hafele = invoice_product.objects.filter(**kwargs,brand=2,name__cancel_inv=False).order_by('name__invoice_date',"-created")
        else:
            hafele = invoice_product.objects.filter(brand=2,name__cancel_inv=False,created__year__gt="2021",created__month__gt="0").order_by('name__delivery_date',"-created")
        return hafele
    def test_func(self):
        return self.request.user.username.startswith(tuple(['hafele','admin']))

class invoiceHflListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/invoice_list_hfl.html'
    model = invoice
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        hafele = self.request.GET.get('hafele')
        kwargs = {}
        if hafele :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): hafele})
        
        if start_date and end_date :
            kwargs.update({'{0}__{1}__{2}'.format('created','date', 'range'): (start_date, end_date)})

        if len(kwargs) >0:
            hafele = invoice_product.objects.filter(**kwargs,brand=13,name__cancel_inv=False).order_by('name__invoice_date',"-created")
        else:
            hafele = invoice_product.objects.filter(brand=13,created__year__gt="2021",created__month__gt="0",name__cancel_inv=False).order_by('name__delivery_date',"-created")
        return hafele
    def get_context_data(self, **kwargs):
        context = super(invoiceHflListView, self).get_context_data(**kwargs)
        # Call the base implementation first to get a context
        commission_hafele = (((F('real_price')*(F('gp'))/100))*F('qty')) + (((F('real_price')/0.8)*0.2)*F('qty'))
        total_commission = self.get_queryset().filter(gp__gte=5,gp__lt=20,created__year__gt="2022").aggregate(total=(Sum(commission_hafele))*(3/100))['total']
        # total_sell_price = 0 if not total_sell_price else total_sell_price
        total_commission = 0 if not total_commission else total_commission


        summary = {
            'total_commission': total_commission,
            # 'vat_pay':((total_sell_price-total_cost)/total_vat)-(total_sell_price-total_cost),
        }
        # Add in the publisher
        context['summary'] = summary
        return context
    
    def test_func(self):
        return self.request.user.username.startswith(tuple(['hfl','admin']))
    
class invoiceLerListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/invoice_list_ler.html'
    model = invoice
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        hafele = self.request.GET.get('hafele')
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        kwargs = {}
        if hafele :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): hafele})
        
        if a :
            kwargs.update({'{0}__{1}'.format('name__ler_receive','icontains'): (a)})

        if b :
            kwargs.update({'{0}__{1}'.format('name__ler_deliver','icontains'): (b)})
    

        if start_date and end_date :
            kwargs.update({'{0}__{1}__{2}'.format('created','date', 'range'): (start_date, end_date)})

        if len(kwargs) >0:
            hafele = invoice_product.objects.filter(**kwargs,name__ler_pickup=True,name__cancel_inv=False).exclude(product__productname="ค่าขนส่ง").exclude(product__productname="ส่วนลด").order_by( 'name__ler_deliver', 'name__ler_receive')
        else:
            hafele = invoice_product.objects.filter(name__ler_pickup=True,created__year__gt="2022",name__cancel_inv=False).exclude(product__productname="ค่าขนส่ง").exclude(product__productname="ส่วนลด").order_by(F('name__ler_deliver').desc(nulls_first=True), F('name__ler_receive').desc(nulls_first=True))
        return hafele
    def get_context_data(self, **kwargs):
        context = super(invoiceLerListView, self).get_context_data(**kwargs)
        # Call the base implementation first to get a context
        profit_overall = (((F('real_price')*(100-F('gp'))/100))*F('qty')) if not (F('real_price')*F('qty')) else (F('real_price')*F('qty'))
        total_profit = self.get_queryset().filter().aggregate(total=(Sum(profit_overall))*(3/100))['total']
        # total_sell_price = 0 if not total_sell_price else total_sell_price
        profit_overall = 0 if not profit_overall else profit_overall


        summary = {
            'profit_overall': profit_overall,
            'total_profit': total_profit,
            # 'vat_pay':((total_sell_price-total_cost)/total_vat)-(total_sell_price-total_cost),
        }
        # Add in the publisher
        context['summary'] = summary
        return context
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))
    
class invoiceLerSendListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/invoice_list_ler_send.html'
    model = invoice
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        hafele = self.request.GET.get('hafele')
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        kwargs = {}
        if hafele :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): hafele})
        
        if a :
            kwargs.update({'{0}__{1}'.format('name__ler_expected_d','icontains'): (a)})

        if b :
            kwargs.update({'{0}__{1}'.format('name__ler_deliver','icontains'): (b)})
    

        if start_date and end_date :
            kwargs.update({'{0}__{1}__{2}'.format('created','date', 'range'): (start_date, end_date)})

        if len(kwargs) >0:
            hafele = invoice_product.objects.filter(**kwargs,name__ler_pickup=True,name__ler_deliver__isnull=True,name__cancel_inv=False).exclude(product__productname="ค่าขนส่ง").exclude(product__productname="ส่วนลด").order_by( 'name__ler_priority','name__invoice_date')
        else:
            hafele = invoice_product.objects.filter(name__ler_pickup=True,created__year__gt="2022",name__ler_deliver__isnull=True,name__cancel_inv=False).exclude(product__productname="ค่าขนส่ง").exclude(product__productname="ส่วนลด").order_by('name__invoice_date')
        return hafele
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))


class invoiceTekaListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/invoice_list_teka.html'
    model = invoice
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): a})
        
        if start_date and end_date :
            kwargs.update({'{0}__{1}__{2}'.format('created','date', 'range'): (start_date, end_date)})

        if len(kwargs) >0:
            hafele = invoice_product.objects.filter(**kwargs,brand=6,created__year__gt="2023",name__cancel_inv=False).order_by('name__invoice_date',"-created")
        else:
            hafele = invoice_product.objects.filter(brand=6,created__year__gt="2023",name__cancel_inv=False).order_by('name__delivery_date',"-created")
        return hafele
    def test_func(self):
        return self.request.user.username.startswith(tuple(['teka','admin']))

class invoiceBekoListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/invoice_list_beko.html'
    model = invoice
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        beko = self.request.GET.get('beko')
        kwargs = {}
        if beko :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): beko})
        
        if start_date and end_date :
            kwargs.update({'{0}__{1}__{2}'.format('created','date', 'range'): (start_date, end_date)})

        if len(kwargs) >0:
            beko = invoice_product.objects.filter(**kwargs,brand=19,name__cancel_inv=False).order_by('name__invoice_date',"-created")
        else:
            beko = invoice_product.objects.filter(brand=19,name__cancel_inv=False,created__year__gt="2023").order_by('name__delivery_date',"-created")
        return beko
    def test_func(self):
        return self.request.user.username.startswith(tuple(['beko','admin']))

class invoicePenkListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/invoice_list_penk.html'
    model = invoice
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        c = self.request.GET.get('c')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): a})

        if b :
            kwargs.update({'{0}__{1}'.format('product__productname', 'icontains'): b})

        if c :
            kwargs.update({'{0}__{1}'.format('name__order_number', 'icontains'): c})

        if start_date and end_date :
            kwargs.update({'{0}__{1}__{2}'.format('created','date', 'range'): (start_date, end_date)})

        if len(kwargs) >0:
            penk = invoice_product.objects.filter(Q(brand=3) | Q(brand = 9),name__cancel_inv=False, **kwargs).order_by('name__delivery_date',"-created")
        else:
            penk = invoice_product.objects.filter(Q(brand=3) | Q(brand = 9),name__cancel_inv=False,created__year__gt="2021",created__month__gt="0").order_by('name__delivery_date',"-created")
        return penk
    def test_func(self):
        return self.request.user.username.startswith(tuple(['penk','admin']))

class invoiceAllView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['paid']
    template_name = 'invoice/all_paid.html'
    success_url = '/invoice/'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))

class invoicePenkView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['invoice_eve','delivery_date','evenote']
    template_name = 'invoice/penk_detail.html'
    success_url = '/invoice/penk'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['penk','admin']))

class invoiceHafeleView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['invoice_eve','delivery_date','evenote']
    template_name = 'invoice/hafele_detail.html'
    success_url = '/invoice/hafele'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['hafele','admin']))

class invoiceHflView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['map_pic','delivery_date','evenote']
    template_name = 'invoice/hfl_detail.html'
    success_url = '/invoice/hfl'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['hfl','admin']))

class invoiceTekaView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['invoice_eve','delivery_date','evenote']
    template_name = 'invoice/teka_detail.html'
    success_url = '/invoice/teka'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['teka','admin']))

class invoiceBekoView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['invoice_eve','delivery_date','evenote']
    template_name = 'invoice/beko_detail.html'
    success_url = '/invoice/beko'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['beko','admin']))
    
class invoiceLerView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['ler_print','ler_receive','ler_deliver','ler_note']
    template_name = 'invoice/ler_detail.html'
    success_url = '/invoice/ler'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))

class invoiceLerSendView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['ler_expected_d','ler_priority','ler_note','ler_map']
    template_name = 'invoice/ler_send_detail.html'
    success_url = '/invoice/lersend'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))

class invoiceView(UpdateView):
    model = invoice
    fields = ['invoice_eve','delivery_date','evenote']
    template_name = 'invoice/eve_detail.html'
    success_url = '/invoice/eve'

def CheckPayment(request):
    if request.method == 'POST':
        form = CheckPaymentForm(request.POST)
        paymentmade = request.POST.get('paymentmade', 0)
        money_collect = request.POST.get('money_collect', 0)


    return render(request, 'invoice/receiveform.html', {'form': CheckPayment})


class etaxListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/etax.html'
    model = invoice
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        q = self.request.GET.get('q')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        c = self.request.GET.get('c')
        d = self.request.GET.get('d')
        f = self.request.GET.get('f')
        g = self.request.GET.get('g')
        h = self.request.GET.get('h')
        i = self.request.GET.get('i')
        kwargs = {}
        if q :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): q})
        if a :
            kwargs.update({'{0}__{1}'.format('name__tel_number', 'icontains'): a})
        if b :
            kwargs.update({'{0}'.format('name__etax'): b})
        if c :
            kwargs.update({'{0}__{1}'.format('name__address', 'icontains'): c})
        if d :
            kwargs.update({'{0}__{1}'.format('name__count_invoice_number', 'icontains'): d})
        if f :
            kwargs.update({'{0}__{1}'.format('name__email_addess', 'icontains'): f})
        if g :
            kwargs.update({'{0}'.format('name__send_etax_email'): g})
        if h :
            kwargs.update({'{0}'.format('money_collect'): h})       
        if i :
            kwargs.update({'{0}'.format('name__invoice_etax'): i})  
        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('name__invoice_date','range'): (start_date, end_date)})
        if len(kwargs) >0:
            listall = invoice_product.objects.filter(Q(**kwargs,name__invoice=True,name__cancel_inv=False,name__invoice_date__year__gt="2023")  | Q(**kwargs,name__invoice=True,name__cancel_inv=False,name__urgent_need_invoice=True)).exclude(name__count_invoice_number = None).order_by("-created")
        else:
            listall = invoice_product.objects.filter(Q(name__cancel_inv=False,name__invoice=True,name__invoice_date__year__gt="2023") | Q(name__cancel_inv=False,name__invoice=True,name__urgent_need_invoice=True)).exclude(name__count_invoice_number = None).order_by("-created")
        return listall
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))
    
class etaxAllView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['etax','send_etax_email']
    template_name = 'invoice/etax_print.html'
    success_url = '/invoice/etax'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))
    

def etaxpaper(request, id):
    detail = get_object_or_404(invoice, id=id)
    total_price = detail.invoices.aggregate(result=Sum(F('sell_price')*F('qty')))['result']
    baht = ThaiBahtConversion(total_price)
    context = {
            'detail':detail,
            'total_price':total_price,
            'baht':baht,
    }

    return render(request,'invoice/detail_etax.html',context)

def etax_done(request, id):
    detail = get_object_or_404(invoice, id=id)
    total_price = detail.invoices.aggregate(result=Sum(F('sell_price')*F('qty')))['result']
    baht = ThaiBahtConversion(total_price)
    context = {
            'detail':detail,
            'total_price':total_price,
            'baht':baht,
    }

    return render(request,'invoice/detail_etax_done.html',context)


class NoetaxListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/noetaxlist.html'
    model = invoice
    paginate_by = 500
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        kwargs = {}
        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('name__invoice_date','range'): (start_date, end_date)})
        if len(kwargs) >0:
            ptst = invoice_product.objects.filter(**kwargs,name__invoice=True,name__invoice_etax=False,created__year__gt="2021",created__month__gt="0").order_by("-created")
        else:
            ptst = invoice_product.objects.filter(name__invoice=True,name__invoice_etax=False,created__year__gt="2022",created__month__gt="0").order_by("-created")
        return ptst

    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))
    


class invoicewithstock_productListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/invoicewithstock_product_list.html'
    model = invoice_product
    ordering = ['date']
    paginate_by = 50
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        c = self.request.GET.get('c')
        d = self.request.GET.get('d')
        e = self.request.GET.get('e')
        f = self.request.GET.get('f')
        s_date = self.request.GET.get('s_date')
        e_date = self.request.GET.get('e_date')
        cs_date = self.request.GET.get('cs_date')
        ce_date = self.request.GET.get('ce_date')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): a})

        if b :
            kwargs.update({'{0}__{1}'.format('brand__brand_name', 'icontains'): b})

        if c :
            kwargs.update({'{0}__{1}'.format('platform', 'icontains'): c})

        if d :
            kwargs.update({'{0}'.format('name__invoice'): d})
        
        if e :
            kwargs.update({'{0}'.format('paymentmade'): e})

        if f :
            kwargs.update({'{0}'.format('money_collect'): f})

        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('name__invoice_date','range'): (start_date, end_date)})

        if s_date and e_date :
            kwargs.update({'{0}__{1}'.format('payment_date','range'): (s_date, e_date)})

        if cs_date and ce_date :
            kwargs.update({'{0}__{1}'.format('collect_date','range'): (cs_date, ce_date)})

        if len(kwargs) >0:
            summary = invoice_product.objects.filter(**kwargs,name__invoice_date__year__gt="2021",name__invoice_date__month__gt="0",name__cancel_inv=False).order_by("-created")
        else:

            summary = invoice_product.objects.filter(name__invoice_date__year__gt="2021",name__invoice_date__month__gt="0",name__cancel_inv=False).order_by("-created")
        return summary
    def get_context_data(self, **kwargs):
        context = super(invoicewithstock_productListView, self).get_context_data(**kwargs)
        total_received = self.get_queryset().aggregate(a=Sum(F('received')*F('qty')))['a']
        total_order = self.get_queryset().aggregate(a=Count('name__order_number',distinct=True))['a']
        total_bill = self.get_queryset().aggregate(a=Sum(F('sell_price')*F('qty')))['a']
        total_tst = self.get_queryset().filter(brand=13).aggregate(tst=Sum(F('received')*F('qty')*0.92))['tst']
        total_received_eve = self.get_queryset().filter(brand=1).aggregate(a=Sum(F('received')*F('qty')))['a']
        total_received_hafele = self.get_queryset().filter(Q(brand=2) | Q(brand = 13)).aggregate(a=Sum(F('received')*F('qty')))['a']
        total_received_mex = self.get_queryset().filter(Q(brand=3) | Q(brand = 9)).aggregate(a=Sum(F('received')*F('qty')))['a']
        total_received_other = self.get_queryset().filter(Q(brand=4) | Q(brand = 5) | Q(brand = 6) | Q(brand = 7) | Q(brand = 8) | Q(brand = 10) | Q(brand = 11)| Q(brand = 12) | Q(brand = 14) | Q(brand = 15)| Q(brand = 16)| Q(brand = 17)).aggregate(a=Sum(F('received')*F('qty')))['a']
        total_received_trasport = self.get_queryset().filter(Q(name__ler_pickup=True)).aggregate(a=Sum(F('real_price')*F('qty')*F('gp')/100))['a']
        cost = (((('100'-F('gp'))*F('real_price')))*F('qty'))
        total_cost = self.get_queryset().aggregate(total=Sum(cost)/100)['total']
        total_received = 0 if not total_received else total_received
        # total_sell_price = 0 if not total_sell_price else total_sell_price
        total_cost = 0 if not total_cost else total_cost
        total_vat = Decimal('1.07')

        summary = {
            'total_received': total_received,
            'total_received_mex':total_received_mex,
            'total_tst':total_tst,
            'total_received_other':total_received_other,
            'total_received_eve':total_received_eve,
            'total_received_hafele':total_received_hafele,
            'profit':total_received - total_cost,
            'percent_profit':(int(1)-(int(1)-(total_received - total_cost)/total_cost))*100 if total_cost != 0 else 0,
            'need_pay':total_cost,
            'total_bill':total_bill,
            'total_order':total_order,
            'total_received_trasport':total_received_trasport,
            # 'vat_pay':((total_sell_price-total_cost)/total_vat)-(total_sell_price-total_cost),
        }
        # Add in the publisher
        context['summary'] = summary
        return context
    def test_func(self):
        return self.request.user.username.startswith('admin')
    


class invoiceall_productListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/all_product_list.html'
    model = invoice_product
    ordering = ['date']
    paginate_by = 50
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        c = self.request.GET.get('c')
        d = self.request.GET.get('d')
        e = self.request.GET.get('e')
        f = self.request.GET.get('f')
        s_date = self.request.GET.get('s_date')
        e_date = self.request.GET.get('e_date')
        cs_date = self.request.GET.get('cs_date')
        ce_date = self.request.GET.get('ce_date')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): a})

        if b :
            kwargs.update({'{0}__{1}'.format('brand__brand_name', 'icontains'): b})

        if c :
            kwargs.update({'{0}__{1}'.format('platform', 'icontains'): c})

        if d :
            kwargs.update({'{0}'.format('name__invoice'): d})
        
        if e :
            kwargs.update({'{0}'.format('paymentmade'): e})

        if f :
            kwargs.update({'{0}'.format('money_collect'): f})

        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('name__invoice_date','range'): (start_date, end_date)})

        if s_date and e_date :
            kwargs.update({'{0}__{1}'.format('payment_date','range'): (s_date, e_date)})

        if cs_date and ce_date :
            kwargs.update({'{0}__{1}'.format('collect_date','range'): (cs_date, ce_date)})

        if len(kwargs) >0:
            summary = invoice_product.objects.filter(**kwargs,name__invoice_date__year__gt="2021",name__invoice_date__month__gt="0",name__cancel_inv=False).order_by("-created")
        else:

            summary = invoice_product.objects.filter(name__invoice_date__year__gt="2021",name__invoice_date__month__gt="0",name__cancel_inv=False).order_by("-created")
        return summary
    def get_context_data(self, **kwargs):
        context = super(invoiceall_productListView, self).get_context_data(**kwargs)
        total_received = self.get_queryset().aggregate(a=Sum(F('received')*F('qty')))['a']
        total_order = self.get_queryset().aggregate(a=Count('name__order_number',distinct=True))['a']
        total_bill = self.get_queryset().aggregate(a=Sum(F('sell_price')*F('qty')))['a']
        total_tst = self.get_queryset().filter(brand=13).aggregate(tst=Sum(F('received')*F('qty')*0.92))['tst']
        total_received_eve = self.get_queryset().filter(brand=1).aggregate(a=Sum(F('received')*F('qty')))['a']
        total_received_hafele = self.get_queryset().filter(Q(brand=2) | Q(brand = 13)).aggregate(a=Sum(F('received')*F('qty')))['a']
        total_received_mex = self.get_queryset().filter(Q(brand=3) | Q(brand = 9)).aggregate(a=Sum(F('received')*F('qty')))['a']
        total_received_other = self.get_queryset().filter(Q(brand=4) | Q(brand = 5) | Q(brand = 6) | Q(brand = 7) | Q(brand = 8) | Q(brand = 10) | Q(brand = 11)| Q(brand = 12) | Q(brand = 14) | Q(brand = 15)| Q(brand = 16)| Q(brand = 17)).aggregate(a=Sum(F('received')*F('qty')))['a']
        total_received_trasport = self.get_queryset().filter(Q(name__ler_pickup=True)).aggregate(a=Sum(F('real_price')*F('qty')*F('gp')/100))['a']
        cost = (((('100'-F('gp'))*F('real_price')))*F('qty'))
        total_cost = self.get_queryset().aggregate(total=Sum(cost)/100)['total']
        total_received = 0 if not total_received else total_received
        # total_sell_price = 0 if not total_sell_price else total_sell_price
        total_cost = 0 if not total_cost else total_cost
        total_vat = Decimal('1.07')

        summary = {
            'total_received': total_received,
            'total_received_mex':total_received_mex,
            'total_tst':total_tst,
            'total_received_other':total_received_other,
            'total_received_eve':total_received_eve,
            'total_received_hafele':total_received_hafele,
            'profit':total_received - total_cost,
            'percent_profit':(int(1)-(int(1)-(total_received - total_cost)/total_cost))*100 if total_cost != 0 else 0,
            'need_pay':total_cost,
            'total_bill':total_bill,
            'total_order':total_order,
            'total_received_trasport':total_received_trasport,
            # 'vat_pay':((total_sell_price-total_cost)/total_vat)-(total_sell_price-total_cost),
        }
        # Add in the publisher
        context['summary'] = summary
        return context
    def test_func(self):
        return self.request.user.username.startswith('admin')
    


class invoiceTecnoListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/invoice_list_tecno.html'
    model = invoice
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): a})
        
        if start_date and end_date :
            kwargs.update({'{0}__{1}__{2}'.format('created','date', 'range'): (start_date, end_date)})

        if len(kwargs) >0:
            hafele = invoice_product.objects.filter(**kwargs,brand=10,created__year__gt="2023",name__cancel_inv=False).order_by('name__invoice_date',"-created")
        else:
            hafele = invoice_product.objects.filter(brand=10,created__year__gt="2023",name__cancel_inv=False).order_by('name__delivery_date',"-created")
        return hafele
    def test_func(self):
        return self.request.user.username.startswith(tuple(['tecno','admin']))

class invoiceTecnoView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['invoice_eve','delivery_date','evenote']
    template_name = 'invoice/tecno_detail.html'
    success_url = '/invoice/tecno'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['tecno','admin']))
    


class invoiceLerReceiveListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/invoice_list_ler_receive.html'
    model = invoice
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        hafele = self.request.GET.get('hafele')

        kwargs = {}
        if hafele :
            kwargs.update({'{0}__{1}'.format('name__invoice_eve', 'icontains'): hafele})

        if len(kwargs) >0:
            hafele = invoice_product.objects.filter(**kwargs,brand=1,name__ler_pickup=True,name__ler_receive__isnull=True,name__cancel_inv=False).exclude(product__productname="ค่าขนส่ง").exclude(product__productname="ส่วนลด").order_by( 'name__ler_priority','-name__ler_receive')
        else:
            hafele = invoice_product.objects.filter(name__ler_pickup=True,brand=1,created__year__gt="2022",name__ler_receive__isnull=True,name__cancel_inv=False).exclude(product__productname="ค่าขนส่ง").exclude(product__productname="ส่วนลด").order_by('-name__ler_receive')
        return hafele
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))
    
class invoiceLerReceiveView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['ler_receive']
    template_name = 'invoice/ler_receive_detail.html'
    success_url = '/invoice/lerreceive'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))
    

def lersend_pic(request, id):
    detail = get_object_or_404(invoice, id=id)
    context = {
            'detail':detail,
    }
    return render(request,'invoice/lersend_pic.html',context)
    
class invoiceLerSendCompleteView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['ler_pic1','ler_pic2','ler_pic3','ler_pic4','ler_pic5','ler_pic6','ler_deliver']
    template_name = 'invoice/ler_sendcomplete_detail.html'
    success_url = '/invoice/lersend'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['admin']))
    

class invoiceBoschListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/invoice_list_bosch.html'
    model = invoice
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        c = self.request.GET.get('c')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): a})
        
        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('name__invoice_date', 'range'): (start_date, end_date)})
        
        if b :
            kwargs.update({'{0}'.format('name__showroom'): b})
        if c :
            kwargs.update({'{0}__{1}'.format('name__delivery_date', 'icontains'): c})

        if len(kwargs) >0:
            bosch = invoice_product.objects.filter(**kwargs,brand=21,created__year__gt="2023",name__cancel_inv=False).order_by("-created","paymentmade")
        else:
            bosch = invoice_product.objects.filter(brand=21,created__year__gt="2023",name__cancel_inv=False).order_by("paymentmade","-created")
        return bosch
    def test_func(self):
        return self.request.user.username.startswith(tuple(['bosch','admin']))

class invoiceBoschView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['invoice_eve','delivery_date','evenote','comment']
    template_name = 'invoice/bosch_detail.html'
    success_url = '/invoice/bosch'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['bosch','admin']))
    

class invoicebshListView(UserPassesTestMixin,ListView):
    template_name = 'invoice/invoice_list_bosch2.html'
    model = invoice
    ordering = ['date']
    paginate_by = 20
    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        kwargs = {}
        if a :
            kwargs.update({'{0}__{1}'.format('name__name', 'icontains'): a})
        
        if start_date and end_date :
            kwargs.update({'{0}__{1}'.format('name__invoice_date', 'range'): (start_date, end_date)})
        
        if b :
            kwargs.update({'{0}'.format('name__showroom'): b})

        if len(kwargs) >0:
            bosch = invoice_product.objects.filter(**kwargs,brand=21,created__year__gt="2023",name__cancel_inv=False).order_by("-created","paymentmade")
        else:
            bosch = invoice_product.objects.filter(brand=21,created__year__gt="2023",name__cancel_inv=False).order_by("paymentmade","-created")
        return bosch
    def test_func(self):
        return self.request.user.username.startswith(tuple(['lerbsh','admin']))

class invoicebshView(UserPassesTestMixin,UpdateView):
    model = invoice
    fields = ['invoice_eve','delivery_date','evenote','comment']
    template_name = 'invoice/bosch_detail2.html'
    success_url = '/invoice/lerbsh'
    def test_func(self):
        return self.request.user.username.startswith(tuple(['lerbsh','admin']))