# Bus Company System in python program implement oop concept

class Company:
    def __init__(self, name, address, type, woner, company_code) -> None:
        self.name = name
        self.address = address,
        self.type = type
        self.woner = woner
        self.company_code = company_code
        self.buses = []
        self.routes = []
        self.drivers = []
        self.counters = []
        self.managers = []
        self.supervisors = []

    def add_driver(self, id, name, licens, age, email):
        driver = Driver(id, name, licens, age, email)
        self.drivers.append(driver)
        
    def get_drivers(self):
        return self.drivers
    
    def add_bus(self, name, isAcciBus, sitNumber, color, brand):
        bus = Busses(name, isAcciBus, sitNumber, color, brand)
        self.buses.append(bus)

    def get_busses(self):
        return self.buses
    
    def add_route(self, root1, root2, root3, root4, root5):
        route = Route(root1, root2, root3, root4, root5)
        self.routes.append(route)

    def get_routes(self):
        return self.routes
    
    def add_counter(self, counter1, counter2, counter3, counter4, counter5):
        counter = Counter(counter1, counter2, counter3, counter4, counter5)
        self.counters.append(counter)

    def get_counter(self):
        return self.counters
    
    def add_manager(self, id, name, address, phone, age, email):
        manager = Manager(id, name, address, phone, age, email)
        self.managers.append(manager)

    def get_manager(self):
        return self.managers
    
    def add_supervisor(self, id, name, address, phone, age, email):
        supervisor = Supervisors(id, name, address, phone, age, email)
        self.supervisors.append(supervisor)

    def get_supervisor(self):
        return self.supervisors



class Busses:
    def __init__(self, name, isAcciBus, sitNumber, color, brand) -> None:
        self.name = name
        self.isAcciBus = isAcciBus
        self.sitNumber = sitNumber
        self.color = color
        self.brand = brand 

    def __repr__(self) -> str:
        return repr({
            'name': self.name,
            'isAcciBus': self.isAcciBus,
            'sitNumber': self.sitNumber,
            'color': self.color,
            'brand': self.brand
        })
    
class Route:
    def __init__(self, root1, root2, root3, root4, root5) -> None:
        self.root1 = root1
        self.root2 = root2
        self.root3 = root3
        self.root4 = root4
        self.root5 = root5 

    def __repr__(self) -> str:
        return repr({
            'root1': self.root1,
            'root2': self.root2,
            'root3': self.root3,
            'root4': self.root4,
            'root5': self.root5
        })

class Driver:
    def __init__(self, id, name, licens, age, email) -> None:
        self.id = id
        self.name = name
        self.licens = licens
        self.age = age
        self.email = email

    def __repr__(self) -> str:
        return repr({
            'id': self.id,
            'name': self.name,
            'licens': self.licens,
            'age': self.age,
            'email': self.email,
        })
    
class Counter:
    def __init__(self, counter1, counter2, counter3, counter4, counter5) -> None:
        self.counter1 = counter1
        self.counter2 = counter2
        self.counter3 = counter3
        self.counter4 = counter4
        self.counter5 = counter5

    def __repr__(self) -> str:
        return repr({
            'counter1': self.counter1,
            'counter2': self.counter2,
            'counter3': self.counter3,
            'counter4': self.counter4,
            'counter5': self.counter5,
        })
    
class Manager:
    def __init__(self, id, name, address, phone, age, email) -> None:
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.age = age
        self.email = email

    def __repr__(self) -> str:
        return repr({
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'phone': self.phone,
            'age': self.age,
            'email': self.email,
        })
    
class Supervisors:
    def __init__(self, id, name, address, phone, age, email) -> None:
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.age = age
        self.email = email

    def __repr__(self) -> str:
        return repr({
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'phone': self.phone,
            'age': self.age,
            'email': self.email,
        })
        

Fleet_Lines = Company('Fleet lines', 'USA', 'Bus Tranportation', 'Habibor Rahaman', '#238984')
Fleet_Lines.add_driver('239833', 'Jems scot', True, 27, 'jemsscot12@gmail.com')
Fleet_Lines.add_driver('839843', 'Allen crow', True, 25, 'allencrow45@gmail.com')
Fleet_Lines.add_bus('Green line', True, 42, 'Silver gray', 'Hino')
Fleet_Lines.add_route('baridhara 102', 'bownani 2', 'mipur 11', 'hatirjhil', 'Shirajdikhan')
Fleet_Lines.add_counter('mirpur 11', 'zatrabari', 'motijhil', 'purbachol', 'mohmmodpur')
Fleet_Lines.add_manager('738747', 'Talad Ahmed', 'Rangpur - Dhaka', '0178923823', 29, 'talad@gmail.com')
Fleet_Lines.add_supervisor('192823', 'Habibor Rahaman', 'Munshigonj - Dhaka', '01732387437', 29, 'habibor1010@gmail.com')

print(Fleet_Lines.get_drivers())
print(Fleet_Lines.get_busses())
print(Fleet_Lines.get_routes())
print(Fleet_Lines.get_counter())
print(Fleet_Lines.get_manager())
print(Fleet_Lines.get_supervisor())

# for loop using into a list of object
for key, value in Fleet_Lines.get_drivers()[0].__dict__.items():
    print(f'{key}: {value}')
print('\n')

# for loop using into a list of object
for x in Fleet_Lines.get_drivers():
    for key, value in x.__dict__.items():
        print(f'{key}: {value}')
    print('\n')

# map using into a list of object
all_drivers = map(lambda x : x.__dict__, Fleet_Lines.get_drivers())
for driver in  all_drivers:
    print(driver)