#tuple in python program...

things = ("bottle", "tripod", "pen", "computer", "camera", "phone", "sunglass")
print(things)
print(type(things))

print(things[0])
print(things[4])
print(things[6])

for item in things:
    print(item)

if "tripod" in things:
    print("Exist")
else:
    print("Dose not exist")

if "hello" in things:
    print("Exist")
else:
    print("Dose not exist")

print(f'Total element of tuple: {len(things)}')

mega = ([23, 45], [54, 78], [19, 74], [8, 5])
print(f'After: {mega}')
mega[0][1] = 99
mega[1][0] = 95
mega[3][0] = 48
mega[3][1] = 68
print(f'Befor: {mega}')