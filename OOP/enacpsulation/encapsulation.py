# Encapsulation implement in python programming language

class Bank:
    def __init__(self, holderName, initialDiposit, age) -> None:
        self.holderName = holderName # public attribute
        self._age = age # protected attribute
        self.__blance = initialDiposit # private attribute

    def diposit(self, amount):
        if(amount <= 0):
                print(f'Your are input 0 or nagative value')
        else:
            self.__blance += amount

    def withdraw(self, amount):
        if(amount > 0 and amount <= self.__blance):
            self.__blance -= amount
        else:
            if(amount <= 0):
                print(f'Your are input 0 or nagative value')
            else:
                print(f'{self.holderName} withdraw blance {amount} is bigger the diposit balance {self.__blance}')
            

    def getBlance(self):
        return (f'Diposit blance is: {self.__blance}')
    
    def __repr__(self) -> str:
        return repr({
            'holderName' : self.holderName, 
            'blance': self.__blance,
            'age': self._age
        })
    

habib = Bank('Habibor Rahaman', 14000, 26)
print(habib.holderName)
habib.diposit(2378)
print(habib.getBlance())
habib.withdraw(3740)
print(habib.getBlance())
habib = habib.__dict__
print(type(habib))
print(habib)
