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
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            print(f'salary can not be nagative') 
        else:
            self.__balance += value




habib = User('144369', 'Habibor Rahaman', 'h23989f783', 33680, 'habibor.rahaman1010@gmail.com')
print(habib.id)
print(habib.email)
print(habib.balance)
habib.balance = 4404
print(habib.balance)