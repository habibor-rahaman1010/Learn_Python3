# Inheritance implement in python using oop concept

class Laptop:
    def __init__(self, model, brand, type, price, color, ram, ssd) -> None:
        self.model = model
        self.brand = brand
        self.type = type
        self.price = price
        self.color = color
        self.ram = ram
        self.ssd = ssd

    def __repr__(self) -> str:
        return ({
            'model': self.model,
            'brand': self.brand,
            'type': self.type,
            'price': self.price,
            'color': self.color,
            'ram': self.ram,
            'ssd': self.ssd,
        })
    
    def run(self):
        print(f'My laptop {self.model} is running right now')
        
    def coding(self):
        print(f'I am right now coding by my {self.model} laptop')

class Phone:
    def __init__(self, model, brand, price, color, ram, dualSime, touchScreen) -> None:
        self.model = model
        self.brand = brand
        self.price = price
        self.color = color
        self.ram = ram
        self.dualSime = dualSime
        self.touchScreen = touchScreen

    def run(self):
        print(f'My phone {self.model} is running right now')
        
    def phone_call(self, number, text):
        print(f'Sending SMS to {number} with text: {text}')
      