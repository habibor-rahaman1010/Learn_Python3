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
