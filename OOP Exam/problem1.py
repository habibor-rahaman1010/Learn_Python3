import math
class Calculation:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def getSum(self):
        return (self.a + self.b + self.c)

    def getFactorial(self):
        return math.factorial(self.b)

obj = Calculation(3, 5, 5)
print(f'Sum is: {obj.getSum()}')
print(f'Factorial is: {obj.getFactorial()}')