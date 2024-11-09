from decimal import Decimal
from django.conf import settings
from product.models import allproduct

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        

        if product_id not in self.cart:
            # Modify by CHutchai on Dec 6,2022 -- To add Brand to each item
            self.cart[product_id] = {'quantity': 0, 
                                    'price': str(product.sale_price),
                                    'brand' : product.brand.brand_name}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        
        # 
        
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_id = self.cart.keys()
        products = allproduct.objects.filter(id__in=product_id)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    # Added on Oct 6,2022 -- To list all product's brand in current cart
    # def get_brand(self):
    #     brands = [self.cart[str(item)]['brand'] for item in self.cart]
    #     # print(list(set(brands))) #Fixed Error 5 problem
    #     # return ' '.join(list(set(brands))) #Fixed Error 5 problem
    #     return ' '.join(brands)

    # def is_mix_brand(self):
    #     print(f'Len {len(self.cart)}')
    #     if len(self.cart) <= 1 :
    #         return 'false'
        
    #     # Case more items
    #     brand =''
    #     mix   ='false'
    #     for ix,item in enumerate(self.cart):
    #         print(ix,self.cart[str(item)]['brand'])
    #         if ix == 0 :
    #             print('Assign first brand name')
    #             brand = self.cart[str(item)]['brand']
    #             continue

    #         if brand != self.cart[str(item)]['brand']:
    #             mix = 'true'
    #             break

    #     print('Not found mix brand')
    #     return mix

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
