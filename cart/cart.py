from products.models import Product


class Cart:

    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart', {})
    
    def add(self, product_id, quantity=1):
        """
        adds product to cart using 
        product id : int

        """
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id] += quantity
        else:
            self.cart[product_id] = quantity
        self.session['cart'] = self.cart

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            if self.cart[product_id] <= 1:
                del self.cart[product_id]
            else:
                self.cart[product_id] -= 1
                print(self.cart[product_id])
                
        self.session['cart'] = self.cart
    
    def clear(self):
        self.session['cart'] = {}

    def list(self):
        
        return Product.objects.filter(id__in=self.cart)
    
    def quantity(self, id):
        return self.cart[str(id)]
    
    def cart_total(self):
        total = 0
        if self.cart:
            for product, amount in self.cart.items():
                items = Product.objects.get(id=product)
                total += items.price * amount
        return total
    
    def cart_item_total(self):
        if self.cart:
            return sum(self.cart.values())
        return 0





                                     