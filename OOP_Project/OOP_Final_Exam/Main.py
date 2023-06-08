# this is my main funtion....
from Bank import Bank
from User import User


def Main():
    # create users
    user_1 = User('144369', 'habibor rahaman', 'habibor12@gmail.com', '123456', 'user')
    user_2 = User('144370', 'tamim anam', 'tamimanam12@gmail.com', '372730', 'user')
    user_1.deposit(3900)

    # check current blance and blance transfer here
    print(user_1.check_available_balance())
    user_1.transfer_amount(2000, user_1, user_2)
    print(user_2.check_available_balance())
    print(user_1.check_available_balance())

    # create a bank
    asia = Bank('Bank Asia', 'bankasia12@gmail.com', 'shirajdikhan, Munshigonj')
    asia.add_user(user_1)
    asia.add_user(user_2)
  

if __name__ == '__main__':
    Main()