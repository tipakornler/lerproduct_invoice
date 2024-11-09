from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView ,DeleteView, UpdateView
from .models import	code
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
# Added by Chutchai on Sep 28,2022 -- To support promo code function for API
def get_promo_info(request,code_name):
    import json
    from promocode.models import code
    codes       = code.objects.filter(name=code_name,activated=True)[:1]
    code_obj    =   None
    code_dict   =   None #Modify on Oct 8,2022 , change from {} to None
    if codes : #if promocode is exist
        code_obj    = codes[0]
        code_dict   ={
                        'code':code_obj.name,
                        'discount_rate':code_obj.discount_rate,
                        'discount_price':code_obj.discount_price,
                        # Added on Oct 3,2022 -- to support new promo concept (min price with brand)
                        'promo_price' : code_obj.promo_price,
                        'brands' : list(code_obj.brands.all().values_list('brand_name', flat=True))
                    }

    response = JsonResponse(code_dict, safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = '*'
    return response


class PromoListView(ListView):
    template_name = 'menu/promo.html'
    model = code
    def get_queryset(self):
        promo = code.objects.filter(show=True).order_by("stop")
        return promo