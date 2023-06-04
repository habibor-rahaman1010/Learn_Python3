# method overriding in python program...

class Person:
    def __init__(self, name, age, height, weight, email) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.email = email

    def eat(self):
        print(f'Eatting all foodable stuff!')

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, email, team, playerType, nationality) -> None:
        self.team = team
        self.playerType = playerType
        self.nationality = nationality
        super().__init__(name, age, height, weight, email)

    def eat(self):
        print(f'{self.name} eatting all halthy food')

    def exercise(self):
        print(f'{self.name} everyday doing exercise and feet her helth!')

    def __repr__(self) -> str:
        return repr({
            'name': self.name,
            'age': self.age,
            'height': self.height,
            'weight': self.weight,
            'email': self.email,
            'team': self.email,
            'playerType': self.playerType,
            'nationality': self.nationality
        })
    
    # operator overloading here...
    def __add__(self, other):
        return self.age + other.age
    
    def __mul__(self, other):
        return self.height * self.height
    
    def __len__(self):
        return self.age
    
    def __gt__(self, other):
        return self.age > other.age


sakib = Cricketer('Sakib all hassan', 38, 5.10, 62, 'sakib@gmail.com', 'Bangladesh', 'All rounder', 'BD')
liton = Cricketer('Liton dash', 29, 5.9, 58, 'liton@gmail.com', 'Bangladesh', 'paise boller', 'BD')
sakib.eat()
sakib.exercise()
print(sakib.__dict__)
print(liton.__dict__)

print(sakib + liton)
print(sakib * liton)
print(len(sakib))
print(sakib > liton)