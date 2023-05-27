#function in python

#function without parameter in python
def myName():
    print("This is Habibor Rahaman")

#function with parameter in python
def giveNmae(name):
    print(f'This is my name with parameter: {name}')

#function with parameter and return value in python
def retunName(name):
    return f'Hello {name}'


def doubleIt(num1, num2):
    num1 = num1 * 2
    num2 = num2 * 2
    return (num1, num2) #return tuple


# all function call here
myName()
name = "Habibor Rahaman"
giveNmae(name)
print(retunName(name))
print(doubleIt(23, 25))