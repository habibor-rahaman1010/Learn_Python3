# loacl and global scope in python program

blance = 3000

def buyThings(item, price):
    global blance
    blance = blance - price
    print(f'blance after buying {item}', blance)


buyThings("Sunglass", 1000)


amount = 3000

def bank(item, price):
    global amount
    price = price - 100
    amount = price - 200
    print(f'blance after buying {item}', amount)


bank("Computer", amount)