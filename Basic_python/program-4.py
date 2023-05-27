#conditional statment in python...
num = 3

if(num < 14):
    print(f'{num} is small then 14')

if(num > 4):
    print(f'{num} is bigger then 4')
else:
    print(f'{num} is small then 4')


age = 23

if(age >= 18):
    print("You can vote this election")
elif(age == 90):
    print("You can vote")
else:
    print("You can not vot in this election")


boss = False
if boss is True:
    print("Hello boss")
elif boss is not True:
    print("hello another!")      

result = 60
if(result >= 80 and result <= 100):
    print(f'You got A+ {result}')
elif(result >= 70 and result < 80):
    print(f'You got A {result}')
elif(result >= 60 and result < 70):
    print(f'You got A- {result}')
elif(result >= 50 and result < 60):
    print(f'You got B {result}')
elif(result >= 40 and result < 50):
    print(f'You got C {result}')
elif(result >= 33 and result < 40):
    print(f'You got D {result}')
else:
    print(f'Yout got F {result}')


#nested if else in python program...
cgpa = 3.40
if(cgpa >= 3.00):
    print("You are good!")
    if(cgpa >= 3.50):
        print("You can eate pizza right now")
        if(cgpa > 3.80):
            print("You are legend")
        else:
            print(f"You have good enoughp {cgpa}")
    else:
        print("ok done")

else:
    print("well done")

