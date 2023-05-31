# create simble bank in python use oop

class Bank:
    def __init__(self, balance) -> None:
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
       
    def get_balance(self):
        return self.balance
    
    def diposit(self, amount):
        if(amount > 0):
            self.balance += amount
            print(f'diposited: {amount}')
            print(f'Current balance: {self.get_balance()}')
        else:
            print(f'Please enter positive number!')


    def withdraw(self, amount):
        if(amount > self.balance):
            print(f'Your withdraw blance {amount} is bigger then current balance {self.get_balance()}, you have can not withdraw!')
        else:
            if(amount >= self.min_withdraw and amount <= self.max_withdraw):
                self.balance -= amount
                print(f'Withdraw amount: {amount}')
                print(f'Current balance: {self.get_balance()}')
            else:
                print(f'You have minimum withdraw: {self.min_withdraw} and maximum withdraw: {self.max_withdraw}')


my_bank = Bank(12000)
print(f'Balance: {my_bank.get_balance()}')
my_bank.diposit(5000)
my_bank.withdraw(16000)
my_bank.diposit(10800)