# This is my bank class...

class Bank:
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.users = []
        self.admins = []
        self.__total_blance = 3560380
        self.__loan_amount = 0

    def add_user(self, user):
        self.users.append(user)

