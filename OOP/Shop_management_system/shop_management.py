# shopping management system implement in python program...

class Product:
    def __init__(self, id, name, price, quantity, category) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def __repr__(self) -> str:
        return repr({
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'category': self.category
        })
    
class Shop:
    def __init__(self, buyerName) -> None:
        self.buyerName = buyerName
        self.cart = []

    def add_prduct(self, id, name, price, quantity, category):
        product = Product(id, name, price, quantity, category)
        self.cart.append(product)

    def buy_product(self, productName):
        have = filter(lambda x : x.__dict__['name'] == productName, self.cart)
        if(len(list(have)) <= 0):
            print(f'{productName} dose not exist in the cart')
        else:
            print(f'{productName} is available you can by this!')

    def __repr__(self) -> str:
        return repr({
            'buyerName': self.buyerName,
            'cart': self.cart
        })

shop = Shop('Habibor Rahaman')
shop.add_prduct('144369', 'hp laptop', 26700, 3, 'laptop')
shop.add_prduct('738734', 'macbok pro', 126700, 3, 'laptop')

shop.buy_product('macbok')
print(shop)


shop2 = Shop('Wahidur Rahaman')
shop2.add_prduct('839843', 'iphone 14', 167000, 3, 'phone')
shop2.add_prduct('563847', 'Air pot', 16389, 3, 'gadget')

shop2.buy_product('Air pot')
print(shop2)