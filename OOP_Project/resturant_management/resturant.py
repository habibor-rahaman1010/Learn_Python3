# a simple restaurant managment system implent in python programming language...

class restaurant:
    def __init__(self, name, address, email, phone) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.owner = []
        self.managers = []
        self.customers = []
        self.cookers = []
        self.food_server = []
        
class Common:
    def __init__(self, name, age, address, email, phone, nid, passport) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        self.phone = phone
        self.nid = nid
        self.passport = passport

class RestaurantOwner(Common):
    def __init__(self, name, age, address, email, phone, nid, passport) -> None:
        super().__init__(name, age, address, email, phone, nid, passport)

class Manager(Common):
    def __init__(self, name, age, address, email, phone, nid, passport) -> None:
        super().__init__(name, age, address, email, phone, nid, passport)

class Customer:
    def __init__(self, name, age, address, email, phone, nid) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        self.phone = phone
        self.nid = nid

class Cooker(Common):
    def __init__(self, name, age, address, email, phone, nid, passport, item_cooking) -> None:
        self.item_cooking = item_cooking
        super().__init__(name, age, address, email, phone, nid, passport)

class Food_Server(Common):
    def __init__(self, name, age, address, email, phone, nid, passport) -> None:
        super().__init__(name, age, address, email, phone, nid, passport)