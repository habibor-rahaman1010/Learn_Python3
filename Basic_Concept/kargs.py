# (advanced) kargs, multiple return from a function

def fullName(fName, lName):
    name = f'{fName} {lName}'
    return name

def professionalName(fName, lName, **addition):
    name = f'{fName} {lName}'
    return (name, addition.items())


#returns multiple things from an function...
def return_lot(n, m):
    sum = n + m
    mul = n * m
    div = n // m
    mod = n % m
    # return [sum, mul, div, mod]
    # return {sum, mul, div, mod}
    return (sum, mul, div, mod)


# all funtion call here
print(fullName("Habibor", "Rahaman"))

#take paramete in order
print(fullName(lName = "Rahaman", fName = "Habibor"))
name = professionalName(fName = "Habibor", lName = "Rahaman", title = "Mr",  surname="Aayan", profession = "Softear Engineer")
for key, value in name[1]:
    print(f'{key} : {value}')

print(return_lot(12, 2))
