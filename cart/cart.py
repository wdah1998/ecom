from store.models import Product, Profile


# from ecom.store.models import Profile


class Cart():
    def __init__(self, request):
        self.session = request.session
        # get request
        self.request = request
        # Try to get the cart from the session
        cart = self.session.get('session_key')

        # If it doesn't exist, create an empty cart dictionary
        if cart is None:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # Deal With Logged in User
        if self.request.user.is_authenticated:
            # get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # convert {'3':1, '2': 4} to {"3":1, "2": 4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # save the carty to the profile model
            current_user.update(old_cart=str(carty))

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # Deal With Logged in User
        if self.request.user.is_authenticated:
            # get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # convert {'3':1, '2': 4} to {"3":1, "2": 4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # save the carty to the profile model
            current_user.update(old_cart=str(carty))

    def cart_total(self):
        # get product ids
        product_ids = self.cart.keys()
        # lookup those keys in our products DB models
        products = Product.objects.filter(id__in=product_ids)
        # get quantities
        quantities = self.cart
        # get counting at 0
        total = 0
        for key, value in quantities.items():
            # convert key string into so we can do math
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)

        return total

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # get ids from cart
        product_ids = self.cart.keys()
        # use ids to lookup product  in DB model
        products = Product.objects.filter(id__in=product_ids)
        # return those  looked up products
        return products

    def get_quant(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        {'4': 3, '2': 5}
        # get cart
        ourcart = self.cart
        # update dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        if self.request.user.is_authenticated:
            # get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # convert {'3':1, '2': 4} to {"3":1, "2": 4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # save the carty to the profile model
            current_user.update(old_cart=str(carty))

        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)
        # delete dictionary/cart

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

        if self.request.user.is_authenticated:
            # get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # convert {'3':1, '2': 4} to {"3":1, "2": 4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # save the carty to the profile model
            current_user.update(old_cart=str(carty))
