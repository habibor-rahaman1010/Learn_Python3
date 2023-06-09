# This is my bank class...

class Bank:
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.users = []
        self.admins = []
        self.__total_blance = 10000
        self.__loan_amount = 0

    def add_user(self, user):
        if(user.get_account_type() == 'user'):
            self.users.append(user)
        else:
            print(f'hello developer user Type kunown')


    def add_admin_user(self, admin):
        if(admin.get_account_type() == 'admin'):
            self.admins.append(admin)
        else:
            print(f'Type kunown')

    def get_bank_blance(self):
        return self.__total_blance

    def loan_from_bank(self, amount, user):
        if(amount < 0):
            print(f'you not loan less then 0')
        elif(amount > user.check_available_balance() * 2):
            print(f'your amount is bigger then your twice blance')
        elif(amount > self.__total_blance):
            print(f'your blance is bigger then bank balance')
        else:
            user.set_user_blance(amount)
            self.__total_blance -= amount
            self.__loan_amount += amount

    def get_bank_loan_amount(self):
        return self.__loan_amount
    