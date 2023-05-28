#string manipulation in python

name = "Habibor Rahaman"
coluigeName = 'Tamim Sahriar Subeen\'s'
text = """
I'm a programmer. how can i help you.
    I learn python right now.
        i have to know many programming laguage.
"""

print(name)
print(coluigeName)
print(text)

# looping in an string 
print(name[0])
print(name[1])

for char in coluigeName:
    print(char)

# array in all char of coluigName
myName = [x for x in name]
print(myName)

print(name[0:5])
print(name[::-1])
print(name[-5:-1])
print(name[0:-7])
print(name[::])
print(name[:5])
print(name[5:])
