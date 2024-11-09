from django.shortcuts import render
from .models import OrderItem, Order, Payment
from .forms import OrderCreateForm, payment
from cart.cart import Cart
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def order_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        address = request.POST.get('address')
        postal_code = request.POST.get('postal_code')
        note = request.POST.get('note')
        grand_price = request.POST.get('grand_price')
        promocode = request.POST.get('promocode')

    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )




            subject = 'คำสั่งซื้อใหม่'
            html_message = render_to_string('cart/maildetail.html', {'cart': cart}) + \
                    '<br>' +first_name + '<br>' + tel + '<br>'+ email + \
                    '<br>'+ address + postal_code + note + \
                    '<br>ราคาที่ต้องชำระ : ' + grand_price + \
                    '<br>Promotion code : ' + promocode + \
                    '<br><B>สามารถชำระเงินได้ที่</B> ธนาคารกสิกรไทย <br>เลขที่บัญชี: 088-3-57389-7 <br> ชื่อบัญชี บริษัท เลอ คอร์ปอเรชั่น จำกัด' 
            plain_message = strip_tags(html_message)
            from_email = 'LerProduct.com <lercorpt@gmail.com>'
            to = ['tipakorn@lerproduct.com',email]

            # print(html_message)
            mail.send_mail(subject, plain_message, from_email, to, html_message=html_message)


        return render(request, 'orders/order/paymentmade.html', {'order': order})
    else:
        form = OrderCreateForm()
        
        # # Added on Oct 8,2022 -- To send brand list to template , to protect Error5 problem
        brands_list = ' '.join([item['brand'] for item in cart])
        total_price =   cart.get_total_price
    return render(request, 'orders/order/create.html', {'form': form ,
                                                'brands_list':brands_list,
                                                'original_price':total_price })


def paymentmade(request) :
    return render(request, 'orders/order/paymentmade.html')

def addpayment(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        payer_name = request.POST.get('payer_name')
        payer_among = request.POST.get('payer_among')
        total_need_to_paid = request.POST.get('total_need_to_paid')
        paid = request.POST.get('paid')
        payer_time = request.POST.get('payer_time')
        payer_date = request.POST.get('payer_date')
  

        payment = Payment(
            payer_name=payer_name,
            payer_among=payer_among,
            total_need_to_paid=total_need_to_paid,
            paid=paid,
            payer_time=payer_time,
            payer_date=payer_date
            ).save()
        cart.clear()

        subject = 'แจ้งโอนเงิน'
        html_message = payer_name + '<br>'+ payer_among + '<br>'+ payer_date + '<br>'+ payer_time
        plain_message = strip_tags(html_message)
        from_email = 'LerProduct.com <lercorpt@gmail.com>'
        to = ['tipakorn@lerproduct.com']

        mail.send_mail(subject, plain_message, from_email, to, html_message=html_message)

        return render(request, 'orders/paid.html', {'form': payment})

def paylater(request):
    cart = Cart(request)
    if request.method == 'POST':
        payer_name = request.POST.get('payer_name')
        total_need_to_paid = request.POST.get('total_need_to_paid')
        paid = request.POST.get('paid')
        
        payment = Payment(
            payer_name=payer_name,
            total_need_to_paid=total_need_to_paid,
            paid=paid
            ).save()
        cart.clear()


        subject = 'ชำระทีหลัง'
        html_message = payer_name + '<br>'+ total_need_to_paid
        plain_message = strip_tags(html_message)
        from_email = 'LerProduct.com <lercorpt@gmail.com>'
        to = ['tipakorn@lerproduct.com']

        mail.send_mail(subject, plain_message, from_email, to, html_message=html_message)
        return render(request, 'orders/paylater.html', {'form': payment})

def showpayment(request):
    return render(request, 'orders/payment.html')