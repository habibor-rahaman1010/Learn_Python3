# Create a banking management system using python OOP in this project...

# create a user class here
class User:
    def __init__(self, unique_id, name, email, password, account_type) -> None:
        self.unique_id = unique_id
        self.name = name
        self.email = email
        self.__password = password
        self.__account_type = account_type
        self.__balance = 0
    
    def deposit(self, amount):
        if(amount < 0):
            print(f'You are given {0} or nagative value {amount}')
        else:
            self.__balance += amount
    
    # this is my user created function
    def create_user_account(self, unique_id, name, email, password, account_type):
        user = User(unique_id, name, email, password, account_type)
        return user

    def withdraw(self, amount):
        if(amount < 0):
            print(f'You can not {0} or nagative value {amount} withdraw')
        elif(amount > self.balance):
            print(f'You can not {amount} withdraw beacuse {amount} is bigger then {self.balance}')
        else:
            self.__balance -= amount

    def check_available_balance(self):
        return self.__balance
    
    def transfer_amount(self, amount, from_user, to_user):
        if(amount < 0):
            print(f'{from_user.name} have not enough mony to transfer {to_user.name}!')
        elif(from_user.check_available_balance() < amount):
            print(f'{from_user.name} transfer amount {amount} bigger then self balance {from_user.check_available_balance()}!')
        else:
            to_user.__balance += amount
            from_user.__balance -= amount










