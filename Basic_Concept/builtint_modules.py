#using basic builtin modules in python
import base64
import uuid
from random import *
from math import *
from datetime import *


name = b'Habibor Rahaman'
encoded = base64.b64encode(name)
print(encoded)
decoded = base64.b64decode(encoded)
print(decoded)

print(uuid.uuid1())
print(uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}'))
rand = random() * 100
print(floor(rand))
print(randint(1, 1000))

choes = choice(['Habibor Rahaman', 'wahidur rahaman', 'rifat', 'arafat', 'shawon'])
print(choes)
