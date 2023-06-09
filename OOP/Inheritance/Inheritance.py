# Inheritance implement in python using oop concept

class Gedget:
    def __init__(self, model, brand, price, color, origin) -> None:
        self.model = model
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    def run(self):
        print(f'My {self.model} is using right now')

class Laptop(Gedget):
    def __init__(self, model, brand, price, color, origin, type, ram, ssd) -> None:
        self.type = type
        self.ram = ram
        self.ssd = ssd
        super().__init__(model, brand, price, color, origin)

    def __repr__(self) -> str:
        return repr({
            'model': self.model,
            'brand': self.brand,
            'type': self.type,
            'price': self.price,
            'color': self.color,
            'origin': self.origin,
            'ram': self.ram,
            'ssd': self.ssd,
        })
        
    def coding(self):
        print(f'I am right now coding by my {self.model} laptop')

class Phone(Gedget):
    def __init__(self, model, brand, price, color, origin, ram, dualSime, touchScreen) -> None:
        self.ram = ram
        self.dualSime = dualSime
        self.touchScreen = touchScreen
        super().__init__(model, brand, price, color, origin)

    def __repr__(self) -> str:
        return repr({
            'model': self.model,
            'brand': self.brand,
            'price': self.price,
            'color': self.color,
            'origin': self.origin,
            'ram': self.ram,
            'dualSime': self.dualSime,
            'touchScreen': self.touchScreen,
        })
        
    def phone_call(self, number, text):
        print(f'Sending SMS to {number} with text: {text}')
      
class Camera(Gedget):
    def __init__(self, model, brand, price, color, origin, pixel) -> None:
        self.pixel = pixel
        super().__init__(model, brand, price, color, origin)

    def __repr__(self) -> str:
        return repr({
            'model': self.model,
            'brand': self.brand,
            'price': self.price,
            'color': self.color,
            'origin': self.origin,
            'pixel': self.pixel,
        })

    def change_lance(self):
        print(f'Yes you can change the lance of your {self.model} camera')


laptop = Laptop('Hp Elitbook 8470p', 'HP', 26500, 'Silver', 'Bangladesh', 'Normal User','hp 8 GB', 'Trancent 256 GB')
phone = Phone('iphone 14', 'Apple', 186000, 'Deep Blue', 'Califonia', '6 GB', True, True)
camara = Camera('Canon D80', 'Canon', 65500, 'Black', 'USA', '20 pixel')

print(laptop)
print(phone)
print(camara)