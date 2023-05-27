#while loop in python program....

initial = 1
while(initial <= 10):
    print(initial)
    initial += 1


#even number findout in python...
i = 2
while(i <= 10):
    if(i % 2 == 0):
        print(i)
    i += 1


#odd number findout in python...
i = 1
while(i <= 10):
    if(i % 2 != 0):
        print(i)
    i += 1

# use break and continue in python program...
j = 1
while(j < 10):
    print(j)
    if(j == 5):
        break
    j += 1

# continue useing in pytohn program...
print("\n")
j = 0
while(j < 10):
    j += 1
    if(j == 5):
        continue
    print(j)

#find out even number using continue in python....
e = 1
while(e <= 10):
    e += 1
    if(e % 2 == 1):
        continue
    print(e)

#find out odd number using continue in python....
e = 0
while(e < 10):
    e += 1
    if(e % 2 == 0):
        continue
    print(e)