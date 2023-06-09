from User import User

class Admin:
    def __init__(self, unique_id, name, email, password, account_type) -> None:
        self.unique_id = unique_id
        self.name = name
        self.email = email
        self.__account_type = account_type
        self.__password = password
        self.__account_type = account_type

    # this is my admin created function
    def create_admin_account(self, unique_id, name, email, password, account_type):
        user = User(unique_id, name, email, password, account_type)
        return user
    
    def available_total_balance(self, bank):
        return bank.get_bank_blance()
    
    def get_account_type(self):
        return self.__account_type
    
    def get_loan_from_bank(self, bank):
        return bank.get_bank_loan_amount()
    
    def off_loan_feature(self):
        print('Off loan feature for all admin and user account')