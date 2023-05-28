#set in python
number = [12, 13, 16, 12, 33, 19, 32, 37, 16, 33]
print(number)

number_set = set(number)
print(number_set)
number_set.add(15)
number_set.add(55)
number_set.add(65)
print(number_set)

number_set.remove(55)
number_set.remove(33)
print(number_set)

for x in number_set:
    print(x)

if 33 in number_set:
    print("Yes")
else:
    print("No")

if 15 in number_set:
    print("Yes")
else:
    print("No")

A = {1, 3, 4, 6, 7}
B = {9, 4, 3, 5, 7}
print(A & B) #uninon
print(A | B) #intersection
print(A - B) #different
print(A ^ B) #symmetric different