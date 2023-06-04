# Abstraction class implement in OOP into python programming language...

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def call(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name, category) -> None:
        self.name = name
        self.category = category
        super().__init__()

    def eat(self):
        return (f'I eating banana')

    def call(self):
        return (f'ow oww kaaa wowww')
    
    def move(self):
        return (f'i move to jumping jumping')

    def __repr__(self) -> str:
        return repr({
            'name': self.name,
            'category': self.category,
            'eat': self.eat(),
            'call': self.call(),
            'move': self.move(),
        })

monkey = Monkey('lilly pot', 'animal')
print(monkey)
