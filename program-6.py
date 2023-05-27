#for loop in pytho program

for x in range(10):
    print(x)

for x in range(1, 11):
    print(x)
    
#even number in python use for loop
for x in range(2, 11, 2):
    print(x)

#even number in python use for loop
for x in range(1, 10, 2):
    print(x)

#for loop into an array
names = ["Habibor Rahaman", "Sobuj", "Tamim", "Wahid", "Talad"]
for name in names:
    print(name)

# add all number of array using for loop
numbers = [12, 23, 56, 78, 54, 23]
sum = 0
for num in numbers:
    sum += num
print(f'Total sum of array: {sum}')

#loop thropt in a string
text = "Hello programmer how can i help you"
for t in text:
    print(t)

#find max value in array
max = numbers[0]
for num in numbers:
    if(max < num):
        max = num
print(f'Max value in array: {max}')