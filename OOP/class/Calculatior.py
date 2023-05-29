# This is my calculator functionality uisng python oop pattern

class Calculator:
    model = 'Casio MS990'

    def Add(seld, *args):
        sum = 0
        for x in args:
            sum += x
        return sum

    def Subtract(self, num1, num2):
        return (num1 - num2)
    
    def Multiply(self, *args):
        mul = 1
        for x in args:
            mul *= x
        return mul
    
    def Divide(self, num1, num2):
        return num1 // num2


myCalculator = Calculator()
print(f'Sum is: {myCalculator.Add(23, 34, 45)}')
print(f'Sub is: {myCalculator.Subtract(45, 15)}')
print(f'Mul is: {myCalculator.Multiply(23, 2)}')
print(f'Div is: {myCalculator.Divide(23, 2)}')