# shopping cart implement in python programming language...

class Shopping:
    cart = []

    def __init__(self, buyer) -> None:
        self.buyer = buyer

    def add_to_cart(self, product):
        self.cart.append(product)

habib = Shopping('Habibor Rahaman')
habib.add_to_cart('Mac book pro')
habib.add_to_cart('Iphone 14')
print(habib.cart)

talab = Shopping('Talab Ahmed')
talab.add_to_cart('T-shirt')
talab.add_to_cart('samsung S23')
print(talab.cart)