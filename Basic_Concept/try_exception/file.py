# file in python program

with open('text.txt', 'a') as file:
    file.write("Hello programmer i learn python \n")

with open('text.txt', 'r') as file:
    readYou = file.read()
    print(readYou)
