# return function and accept a function as a parameter in python program...

def func_decker():
    print(f'Hello programmer i learn python program')
    def notification():
        print(f'all programmer are humble and ginious in erth')
        return (f'my favourit language is C# and javaScript and python')
    return notification

print(func_decker()())
print('\n')
def myFunc(work):
    print('i loved programming and thinking')
    print(work()())
    print(f'computer programming is everywhere')

myFunc(func_decker)