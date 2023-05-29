# create a pen class using python oop methods

class Pen:
    def __init__(self, name, category, color, type, price) -> None:
        self.name = name
        self.category = category
        self.color = color
        self.type = type
        self.price = price


my_pen = Pen('Matador boll point', 'Reguler pen', ['red', 'yello', 'blue', 'gree'], 'boll point', 5)
my_pen2 = Pen('Matador high school', 'Reguler pen', ['red', 'yello', 'blue', 'gree'], 'boll point', 5)
my_pen3 = Pen('Read line point', 'Reguler pen', ['red', 'yello', 'blue', 'gree'], 'boll point', 5)
my_pen4 = Pen('good luck boll point', 'Reguler pen', ['red', 'yello', 'blue', 'gree'], 'boll point', 5)

print(my_pen.name, my_pen.category, my_pen.color, my_pen.type, my_pen.price)
print(my_pen2.name, my_pen2.category, my_pen2.color, my_pen2.type, my_pen2.price)
print(my_pen3.name, my_pen3.category, my_pen3.color, my_pen3.type, my_pen3.price)
print(my_pen4.name, my_pen4.category, my_pen4.color, my_pen4.type, my_pen4.price)