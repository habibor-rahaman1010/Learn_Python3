# this is my main funtion....
from Bank import Bank
from User import User
from Admin import Admin


def Main():
    # create a bank
    asia = Bank('Bank Asia', 'bankasia12@gmail.com', 'shirajdikhan, Munshigonj')
    print(f'__________THIS IS MY {asia.name} ______________')
    # create users
    user_1 = User('144369', 'habibor rahaman', 'habibor12@gmail.com', '123456', 'user')
    user_2 = User('144370', 'tamim anam', 'tamimanam12@gmail.com', '372730', 'user')
    user_3 = User('144371', 'wahidur rahman', 'wahidur12@gmail.com', '8493784', 'user')
    user_4 = User('144369', 'habibor rahaman', 'habibor12@gmail.com', '123456', 'user')
    user_5 = User('144370', 'tamim anam', 'tamimanam12@gmail.com', '372730', 'user')
    user_6 = User('144371', 'wahidur rahman', 'wahidur12@gmail.com', '8493784', 'user')
    

    #create admin users
    admin_1 = Admin('8923h2w3874', 'habibor rahaman', 'habibor12@gmail.com', 'uiweui32u4', 'admin')
    admin_2 = Admin('sahd92839hf', 'tamim anam', 'tamimanam12@gmail.com', 'hbfbh324ruj', 'admin')
    admin_3 = Admin('sdoifj8203h', 'wahidur rahman', 'wahidur12@gmail.com', 'hsfg8237g', 'admin')

    #add deposit all of user
    user_1.deposit(4000)
    user_2.deposit(3000)
    user_3.deposit(2000)

    # check current blance and blance transfer here
    print(user_1.check_available_balance())
    print(user_2.check_available_balance())
    print(user_3.check_available_balance())
    user_1.transfer_amount(1300, user_1, user_2)
    user_2.transfer_amount(8000, user_2, user_1)
    user_3.transfer_amount(700, user_3, user_2)
   

    # create a bank and add user in this bank
    asia.add_user(user_1)
    asia.add_user(user_2)
    asia.add_user(user_3)
    asia.add_user(user_4)
    asia.add_user(user_5)
    asia.add_user(user_6)

    # register all admin in bank system
    asia.add_admin_user(admin_1)
    asia.add_admin_user(admin_2)
    asia.add_admin_user(admin_3)

    #print my all user here
    print('___________________HERE IS MY ALL USERS__________________\n')
    for user in asia.users:
        print(f'name: {user.name} email: {user.email}  type: {user.get_account_type()}')
    print('\n')

    #history checking here
    print('______________THIS IS MY USER TRANSACTION HISTORY_________________\n')
    user_1.withdraw(30)
    user_2.withdraw(50)
    user_2.withdraw(700)
    user_3.withdraw(1350)
    user_3.deposit(70)
    user_2.deposit(1700)
    user_2.transaction_history() 
    print('\n')
    user_1.transaction_history()
    print('\n')
    user_3.transaction_history()
    print('\n')

   # loan from bang a user
    print('____________LOAN FROM BANK TO USER_____________')
    print(f'before current bank balance: {asia.get_bank_blance()}')
    asia.loan_from_bank(1200, user_1)
    print(f'after current bank balance: {asia.get_bank_blance()}')
    print(f'right now user current blance: {user_1.check_available_balance()} \n')

    print(f'before current bank balance: {asia.get_bank_blance()}')
    asia.loan_from_bank(1400, user_2)
    print(f'after current bank balance: {asia.get_bank_blance()}')
    print(f'right now user current blance: {user_2.check_available_balance()}\n')

    print(f'before current bank balance: {asia.get_bank_blance()}')
    asia.loan_from_bank(1800, user_3)
    print(f'after current bank balance: {asia.get_bank_blance()}')
    print(f'right now user current blance: {user_3.check_available_balance()}\n')
  

    #here all admins action in this project...
    #print my all user here
    print('___________________HERE IS MY ALL ADMIN USERS__________________\n')
    for admin in asia.admins:
        print(f'name: {admin.name} email: {admin.email}  type: {admin.get_account_type()}')
    print('\n')

    # check total balane in this bank through out the admin
    print('_________________HERE BANK LOAN AND TOTAL AMOUNT SHOWING_______________')
    print(f'bank total available blance: {admin_1.available_total_balance(asia)}')
    print(f'bank loan amount: {admin_1.get_loan_from_bank(asia)}')
    admin_1.off_loan_feature()



if __name__ == '__main__':
    Main()