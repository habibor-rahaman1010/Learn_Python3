# multi level inheritance in python programming language

class Vehicle:
    def __init__(self, name, price, origin, color) -> None:
        self.name = name
        self.price = price
        self.origin = origin
        self.color = color

class Bus(Vehicle):
    def __init__(self, name, price, origin, color, seat) -> None:
        self.seat = seat
        super().__init__(name, price, origin, color)

class Truck(Vehicle):
    def __init__(self, name, price, origin, color, load, enginType) -> None:
        self.load = load
        self.enginType = enginType
        super().__init__(name, price, origin, color)

class AcciBus(Bus):
    def __init__(self, name, price, origin, color, seat, wifi, temperature, ticket) -> None:
        self.wifi = wifi
        self.temperature = temperature
        self.ticket = ticket
        super().__init__(name, price, origin, color, seat)

class SpecialTruck(Truck):
    def __init__(self, name, price, origin, color, load, enginType, wifi, temperature) -> None:
        self.wifi = wifi
        self.temperature = temperature
        
        super().__init__(name, price, origin, color, load, enginType)

class VipBus(AcciBus):
    def __init__(self, name, price, origin, color, seat, wifi, temperature, ticket, security, enginType) -> None:
        self.security = security
        self.enginType = enginType
        super().__init__(name, price, origin, color, seat, wifi, temperature, ticket)

    def __repr__(self) -> str:
        return repr({
            'name': self.name,
            'price': self.price,
            'origin': self.origin,
            'color': self.color,
            'seat': self.seat,
            'wifi': self.wifi,
            'temperature': self.temperature,
            'ticket': self.ticket,
            'security': self.security,
            'enginType': self.enginType,
        })


greenLine = VipBus('Green Line', 7500000, 'Bangladesh', 'green and silver', 25, True, '18 digree', True, True, 'Diesel')
print(greenLine)