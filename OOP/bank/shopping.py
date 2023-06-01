# shopping cart implement in python program use oop concept

class Shopping:
    def __init__(self, name) -> None:
        self.name = name
        self.cart = []

    def add_To_Cart(self, item_name, price, quantity):
        product = {
            'item': item_name,
            'price': price,
            'quantity': quantity
        }
        self.cart.append(product)


    def product_price(self):
        total = map(lambda x : x['price'] * x['quantity'], self.cart)
        total_price = 0
        for x in list(total):
            total_price += x
        return total_price

    def checkout(self, amout, name):
        if(self.name == name):
            if(self.product_price() == amout):
                print(f'Your purches done {self.name}')


habib = Shopping("habibor Rahaman")
habib.add_To_Cart('Iphone', 120000, 3)
habib.add_To_Cart('Lapto', 60000, 2)
habib.add_To_Cart('Hade Phone', 30000, 3)
habib.add_To_Cart('Ram', 7000, 10)
print(f'{habib.name} total price is: {habib.product_price()}')
habib.checkout(habib.product_price(), habib.name)

rifat = Shopping("Rifat Ahmed")
rifat.add_To_Cart('T-shirt', 270, 4)
rifat.add_To_Cart('Head Phone', 2280, 1)
rifat.add_To_Cart('mouse pade', 70, 5)
print(f'{rifat.name} total price is: {rifat.product_price()}')
rifat.checkout(rifat.product_price(), rifat.name)

jhon = Shopping('Jhone week')
jhon.add_To_Cart('Mercidies Benze', 27050875, 12)
jhon.add_To_Cart('Instrument', 36000, 2)
jhon.add_To_Cart('Machin Gun', 147860, 3)
print(f'{jhon.name} total price is: {jhon.product_price()}')
jhon.checkout(jhon.product_price(), jhon.name)