# lambda expression in python program...

def double(x):
    return x * 2


#lambda funtion in here
getSum = lambda x, y : x + y
getMul = lambda x, y : x * y

name = ['Tom', 'Dog', 'Beear', 'Bee', 'Deer']
name.sort()
print(name)

name2 = ['Tom', 'Dog', 'Beear', 'Bee', 'Deer']
name2.sort(key = lambda x : len(x))
print(name2)


# call all function here
print(double(20))
print(getSum(12, 34))
print(getMul(12, 34))