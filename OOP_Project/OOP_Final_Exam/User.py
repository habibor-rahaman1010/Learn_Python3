# Create a banking management system using python OOP in this project...
from History import History
from Bank import Bank

# create a user class here
class User:
    def __init__(self, unique_id, name, email, password, account_type) -> None:
        self.unique_id = unique_id
        self.name = name
        self.email = email
        self.__password = password
        self.__account_type = account_type
        self.__balance = 0
        self._history = []
    
    def deposit(self, amount):
        if(amount < 0):
            print(f'You are given {0} or nagative value {amount}')
        else:
            self.__balance += amount
            history = History(self.name, self.check_available_balance(), 0, amount, 0)
            self._history.append(history)
    
    # this is my user created function
    def create_user_account(self, unique_id, name, email, password, account_type):
        user = User(unique_id, name, email, password, account_type)
        return user

    def withdraw(self, amount):
        if(amount < 0):
            print(f'You can not {0} or nagative value {amount} withdraw')
        elif(amount > self.__balance):
            print(f'You can not {amount} withdraw beacuse {amount} is bigger then {self.__balance}')
        else:
            self.__balance -= amount
            history = History(self.name, self.check_available_balance(), amount, 0)
            self._history.append(history)

    def check_available_balance(self):
        return self.__balance
    
    def set_user_blance(self, amount):
        self.__balance += amount

    def get_account_type(self):
        return self.__account_type
    
    def transfer_amount(self, amount, from_user, to_user):
        if(amount < 0):
            print(f'{from_user.name} have not enough mony to transfer {to_user.name}!')
        elif(from_user.check_available_balance() < amount):
            print(f'{from_user.name} transfer amount {amount} bigger then self balance {from_user.check_available_balance()}!')
        else:
            to_user.__balance += amount
            from_user.__balance -= amount
            history = History(self.name, self.check_available_balance(), 0, 0, amount)
            self._history.append(history)

    def transaction_history(self):
        for x in self._history:
            print(f'name: {x.name}, amoutn: {x.amount} withdraw: {x.widthraw} diposit: {x.diposit} transfer: {x.transfer}')
