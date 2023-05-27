# even and odd number return in a single function

numbers = [12, 34, 45, 67, 64, 56, 78, 49, 99, 100]

def getEvenOdd(array):
    even = []
    odd = []
    for number in array:
        if(number % 2 == 0):
            even.append(number)
        else:
            odd.append(number)
    return(even, odd)

print(getEvenOdd(numbers))

#sort way to findout odd number in list
odd = [int(num) for num in numbers if(num % 2 == 0)]
print(odd)

#sort way to findout even number in list
even = [int(num) for num in numbers if(num % 2 == 1)]
print(even)


#nested for loop in python
players = ["Sakib", "Misfiq", "Liton"]
ages = [38, 35, 31]

player_comb = []
for player in players:
    for age in ages:
        player_comb.append([player, age])

print(player_comb)

#sort way to nested loop in python program...
player_comb2 = [[player, age] for player in players for age in ages]
print(player_comb2)
