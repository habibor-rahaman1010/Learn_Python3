# Constructor in python program

class Phone:
    def __init__(self, price, category, brand, owner) -> None:
        self.price = price
        self.category = category
        self.brand = brand
        self.owner = owner


my_phone = Phone(12000, 'smart phone', 'apple', 'habibor rahaman')
print(my_phone.price, my_phone.category, my_phone.brand, my_phone.owner)