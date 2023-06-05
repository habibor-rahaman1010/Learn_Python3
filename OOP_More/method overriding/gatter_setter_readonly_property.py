# Getter Setter and Read only property Using Property Decorator in python

class User:
    def __init__(self, id, name, password, balance, email) -> None:
        self.__id = id
        self._name = name
        self.___password = password
        self.__balance = balance
        self.___email = email

    @property
    def id(self):
        return self.__id
    
    @property
    def email(self):
        return self.___email
    
    @property
    def balnce(self):
        return self.__balance



habib = User('144369', 'Habibor Rahaman', 'h23989f783', 33680, 'habibor.rahaman1010@gmail.com')
print(habib.id)
print(habib.email)
print(habib.balnce)