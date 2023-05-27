#default parameter in python program...
def summation(num1 = 0, num2 = 0, num3 = 0):
    result = (num1 + num2 + num3)
    return result


#unlimited argument in this function...
def addNumbers(*args):
    sum = 0
    for number in args:
        sum += number
    return sum

#saparate and unlimited argument in this function...
def allSum(num1 = 0, num2 = 0, *args):
    sum = 0
    for number in args:
        sum += number
    return ((num1 + num2), sum)


# call all funtion in this plase
print(summation(23, 11, 12))
print(addNumbers(12, 34, 56, 67))
print(allSum(42, 34, 56, 67, 34, 32))
