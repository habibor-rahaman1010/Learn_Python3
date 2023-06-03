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
        return repr({
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

    def __repr__(self) -> str:
        return repr({
            'model': self.model,
            'brand': self.brand,
            'price': self.price,
            'color': self.color,
            'ram': self.ram,
            'dualSime': self.dualSime,
            'touchScreen': self.touchScreen,
        })

    def run(self):
        print(f'My phone {self.model} is running right now')
        
    def phone_call(self, number, text):
        print(f'Sending SMS to {number} with text: {text}')
      
class Camera:
    def __init__(self, model, brand, price, color, pixel) -> None:
        self.model = model
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel

    def __repr__(self) -> str:
        return repr({
            'model': self.model,
            'brand': self.brand,
            'price': self.price,
            'color': self.color,
            'pixel': self.pixel,
        })

    def run(self):
        print(f'My camera {self.model} is using right now')

    def change_lance(self):
        print(f'Yes you can change the lance of your {self.model} camera')


laptop = Laptop('Hp Elitbook 8470p', 'HP', 'Normal User', 26500, 'Silver', 'hp 4 GB', 'Trancent 256 GB')
phone = Phone('iphone 14', 'Apple', 186600, 'Blue Black', '8 GB', True, True)
camara = Camera('Canon D80', 'Canon', 65500, 'Black', '20 pixel')

print(laptop)
print(phone)
print(camara)