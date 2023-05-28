#dictionary in python...
person = {
    'name': 'Habibor Rahaman',
    'age': 23,
    'address': 'Mundhigonj, Dhaka',
    'profession': 'Student',
    'department': "Compueter science and engineering"
    }
print(person['department'])
print(person['name'])
person['address'] = "Mohammodpur - Dhaka 1207"
print(person)
print(person.values())
print(person.keys())

for [key, value] in person.items():
    print(f'{key} : {value}')

print(person.items())

for (keys, values) in person.items():
    print(f'{keys} : {values}')

print(person.items())