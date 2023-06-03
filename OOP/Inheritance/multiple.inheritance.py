# multiple inheritance in pytho program...

class Person:
    def __init__(self, name, age, email) -> None:
        self.name = name
        self.age = age
        self.email = email

class School:
    def __init__(self, id, level, address) -> None:
        self.id = id
        self.level = level
        self.address = address

class Sports:
    def __init__(self, game, time) -> None:
        self.game = game
        self.time = time

class Books:
    def __init__(self, bookName, writer, page, color) -> None:
        self.bookName = bookName
        self.writer = writer
        self.page = page
        self.color = color

class Student(Person, School, Sports, Books):
    def __init__(self, name, age, email, id, level, address, game, time, bookName, writer, page, color) -> None:
        Person.__init__(self, name, age, email)
        School.__init__(self, id, level, address)
        Sports.__init__(self, game, time)
        Books.__init__(self, bookName, writer, page, color)
        
    def __repr__(self) -> str:
        return repr({
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'id': self.id,
            'level': self.level,
            'address': self.address,
            'game': self.game,
            'time': self.time,
            'bookName': self.bookName,
            'writer': self.writer,
            'page': self.page,
            'color': self.color,
        })


# object create and print

habib = Student('Habibor Rahaman', 23, 'habibor1010@gmail.com', 144369, 'Bsc in CSE', 'Munshigonj - Dhaka', 'PES foot ball', '5:34:10', 'Steal Like An Artist', 'Seal colen', 220, 'black')
print(habib)
