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

if person['address'] in person['address']:
    print('exist')
else:
    print('does not exist')

if 'Mohammodpur - Dhaka 1207' in person['address']:
    print('exist')
else:
    print('does not exist')

if 'address' in person:
    print('exist')
else:
    print('does not exist')

print(person.get('department'))

computer = [('name', 'computer'), ('ram', '16 gb'), ('processor', 'core i 5'), ('ssd', 512), ('hdd', '1tb')]
obj = dict(computer)
print(obj)
for index, value in enumerate(obj.values()):
    print(f'{index} : {value}')

for index, value in enumerate(obj.keys()):
    print(f'{index} : {value}')
