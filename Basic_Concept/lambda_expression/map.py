# map implement in python programming language

age = [12, 14, 15, 10, 17, 11]
age_double = map(lambda x : x * 2, age)
print(list(age_double))

#map using into an lint
make_double = lambda x : x * 2
get_double = map(make_double, age)
print(list(get_double))

#fruits array perticuler element length find out
fruits = ['mengo', 'banana', 'lichi', 'water mellon', 'apple']
def get_count(x):
    return len(x)

fruitsLen = map(get_count, fruits)
print(list(fruitsLen))

#fruits array perticuler element length find out
fruitsLen2 = map(lambda x : len(x), fruits)
print(list(fruitsLen2))


artist = [
    {'name': 'justin beiber', 'age': 29, 'email': 'justin@gmail.com'},
    {'name': 'Allen walker', 'age': 36, 'email': 'allen@gmail.com'},
    {'name': 'selina gomez', 'age': 25, 'email': 'selina@gmail.com'},
    {'name': 'martin beiber', 'age': 37, 'email': 'martin@gmail.com'},
    {'name': 'ostin beiber', 'age': 43, 'email': 'ostin@gmail.com'},
    {'name': 'lily pots', 'age': 30, 'email': 'lily@gmail.com'},
]

allArtist = map(lambda x : x, artist)
print(list(allArtist))

youngArtist = filter(lambda x : x['age'] < 30, artist)
print(list(youngArtist))
