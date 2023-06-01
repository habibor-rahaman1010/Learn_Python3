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

    def checkout(self, amount):
        total = map(lambda x : x['price'] * x['quantity'], self.cart)
        total_price = 0
        for x in list(total):
            total_price += x
        print(f'Total Price of {self.name}: {total_price}')
        if(amount < total_price):
            print(f'Please provide {total_price - amount} more! \n')
        else:
            extra = amount - total_price
            print(f'Here is your producs and extra mony {extra} \n')

    def remove_item(self, item):
        p = False
        for product in self.cart:
            if(product['item'] == item):
                self.cart.remove(product)
                p = True
                
        if(p == True):
            print(f'Product removed!')
        else:
            print(f'Product dose not exist!')


    def product_list(self):
        for x in self.cart:
            print(x)

habib = Shopping("Habibor Rahaman")
habib.add_To_Cart('Iphone', 120000, 3)
habib.add_To_Cart('Laptop', 60000, 2)
habib.add_To_Cart('Hade Phone', 30000, 3)
habib.add_To_Cart('Ram', 7000, 10)
habib.checkout(530434)
habib.remove_item(habib.cart[0]['item'])
habib.product_list()

rifat = Shopping("Rifat Ahmed")
rifat.add_To_Cart('T-shirt', 270, 4)
rifat.add_To_Cart('Head Phone', 2280, 1)
rifat.add_To_Cart('mouse pade', 70, 5)
rifat.checkout(67236)
rifat.remove_item('mouse pade')
rifat.product_list()

jhon = Shopping('Jhone week')
jhon.add_To_Cart('Mercidies Benze', 27050875, 3)
jhon.add_To_Cart('Instrument', 36000, 2)
jhon.add_To_Cart('Machin Gun', 147860, 3)
jhon.checkout(72837733)
jhon.remove_item('alchohol')
jhon.product_list()
