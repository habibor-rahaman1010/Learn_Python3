#static methods and static attribute in python

class Shopping:
    cart = [] # static property
    origin = 'bangladesh'
    def __init__(self, name, location) -> None:
        self.name = name # instance attribute
        self.loation = location # instance attribute

    def purchaes(self, item, price, amount):
        remaining = amount - price
        print(f'buying {item} for price {price} and reamining {remaining}')

    @classmethod
    def buyProduct(self, item, price, amount):
        remaining = amount - price
        print(f'buying {item} for price {price} and reamining {remaining}')

    @staticmethod
    def purchesProduct(item, price, amount):
        remaining = amount - price
        print(f'buying {item} for price {price} and reamining {remaining}')


Shopping.buyProduct('Laptop', 25700, 26000)
Shopping.purchesProduct('iphon', 72873, 30203)

shop = Shopping('Habibor Rahaman', 'bangladesh')
shop.purchaes('computer', 34000, 43233)

