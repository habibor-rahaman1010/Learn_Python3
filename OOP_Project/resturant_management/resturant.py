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
        self.food_servers = []

    def __repr__(self) -> str:
        return repr({
            'name': self.name,
            'address': self.address,
            'email': self.email,
            'phone': self.phone,
            'owner': self.owner,
            'managers': self.managers,
            'customers': self.customers,
            'cookers': self.cookers,
            'food_servers': self.food_servers,
        })

    def add_owner(self, name, age, address, email, phone, nid, passport):
        owner = RestaurantOwner(name, age, address, email, phone, nid, passport)
        self.owner.append(owner)

    def add_managers(self, name, age, address, email, phone, nid, passport):
        manager = Manager(name, age, address, email, phone, nid, passport)
        self.managers.append(manager)

    def add_customers(self, name, age, address, email, phone, nid):
        coustomer = Customer(name, age, address, email, phone, nid)
        self.customers.append(coustomer)

    def add_cookers(self, name, age, address, email, phone, nid, passport, item_cooking):
        cooker = Cooker(name, age, address, email, phone, nid, passport, item_cooking)
        self.cookers.append(cooker)

    def add_food_server(self, name, age, address, email, phone, nid, passport, start_location, end_location, hub):
        food_server = Food_Server(name, age, address, email, phone, nid, passport, start_location, end_location, hub)
        self.food_servers.append(food_server)

        
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

    def __repr__(self) -> str:
        return repr({
            'name': self.name,
            'age': self.age,
            'address': self.address,
            'email': self.email,
            'phone': self.phone,
            'nid': self.nid,
            'passport': self.passport,
        })

class Manager(Common):
    def __init__(self, name, age, address, email, phone, nid, passport) -> None:
        super().__init__(name, age, address, email, phone, nid, passport)

    def __repr__(self) -> str:
        return repr({
            'name': self.name,
            'age': self.age,
            'address': self.address,
            'email': self.email,
            'phone': self.phone,
            'nid': self.nid,
            'passport': self.passport,
        })

class Customer:
    def __init__(self, name, age, address, email, phone, nid) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        self.phone = phone
        self.nid = nid

    def __repr__(self) -> str:
        return repr({
            'name': self.name,
            'age': self.age,
            'address': self.address,
            'email': self.email,
            'phone': self.phone,
            'nid': self.nid,
        })

class Cooker(Common):
    def __init__(self, name, age, address, email, phone, nid, passport, item_cooking) -> None:
        self.item_cooking = item_cooking
        super().__init__(name, age, address, email, phone, nid, passport)

    def __repr__(self) -> str:
        return repr({
            'name': self.name,
            'age': self.age,
            'address': self.address,
            'email': self.email,
            'phone': self.phone,
            'nid': self.nid,
            'passport': self.passport,
            'item_cooking': self.item_cooking
        })

class Food_Server(Common):
    def __init__(self, name, age, address, email, phone, nid, passport, start_location, end_location, hub) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.hub = hub
        super().__init__(name, age, address, email, phone, nid, passport)

    def __repr__(self) -> str:
        return repr({
            'name': self.name,
            'age': self.age,
            'address': self.address,
            'email': self.email,
            'phone': self.phone,
            'nid': self.nid,
            'passport': self.passport,
            'start_location': self.start_location,
            'end_location': self.end_location,
            'hub': self.hub,
        })


Gloria_Jean = restaurant('Gloria Jean\'s Coffees', 'Gulshan-2', 'gloriajens12@gmail.com', '01739823341')
Gloria_Jean.add_owner('Habibor Rahaman', 23, 'mohammodpur - dhaka', 'habibor12@gamil.com', '01722378432', '18291823239', 'EM:812398')
Gloria_Jean.add_managers('Rifat Ahmed', 23, 'wari - dhaka', 'rifatahmed12@gamil.com', '01392238734', '8912389213', 'EM:673677')
Gloria_Jean.add_customers('Arafat Ahmed', 23, 'zurain - dhaka', 'arafatahmed723@gamil.com', '01829333443', '672387347')
Gloria_Jean.add_cookers('Arafat Ahmed', 23, 'zurain - dhaka', 'arafatahmed723@gamil.com', '01829333443', '672387347', 'EM:728374', ['fish curry', 'mutton resala', 'chiken biriyani', 'franch fry'])
Gloria_Jean.add_food_server('Habibor Rahaman', 23, 'mohammodpur - dhaka', 'habibor12@gamil.com', '01722378432', '18291823239', 'EM:812398', 'warri', 'mohammodpur', 'Dhaka')

print(Gloria_Jean)
