# Polymorphism implement in python program...

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def makeSound(self):
        print(f'Animal makig some sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def makeSound(self):
        print(f'{self.name} calling mew... mewo...')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def makeSound(self):
        print(f'{self.name} calling ghew... ghew...')


class Man(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def makeSound(self):
        print(f'{self.name} calling to copy all animals!')

cat = Cat('pussy cat')
cat.makeSound()

dog = Dog('Tommy')
dog.makeSound()

kaloMiya = Man('kalo miya')
kaloMiya.makeSound()

animals = [cat, dog, kaloMiya]
for x in animals:
    x.makeSound()