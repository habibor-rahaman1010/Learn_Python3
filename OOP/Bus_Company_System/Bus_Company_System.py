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
        self.transports = []

    def Add_Driver(self, id, name, licens, age, email):
        driver = Driver(id, name, licens, age, email)
        self.drivers.append(driver)
        
    def get_drivers(self):
        return self.drivers

    
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
        

Fleet_Lines = Company('Fleet lines', 'USA', 'Bus Tranportation', 'Habibor Rahaman', '#238984')
Fleet_Lines.Add_Driver('239833', 'Jems scot', True, 27, 'jemsscot12@gmail.com')
Fleet_Lines.Add_Driver('839843', 'Allen crow', True, 25, 'allencrow45@gmail.com')
print(Fleet_Lines.get_drivers())