# (advanced) kargs, multiple return from a function

#take paramete in order
def fullName(fName, lNmae):
    name = f'{fName} {lNmae}'
    return name



# all funtion call here
print(fullName("Habibor", "Rahaman"))
print(fullName(lNmae = "Rahaman", fName = "Habibor"))
