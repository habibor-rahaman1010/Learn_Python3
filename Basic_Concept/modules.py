# heare some workable function writing

def addition(num1, num2):
    return(num1 + num2)

def substraction(num1, num2):
    return(num1 - num2)

def multiplication(num1, num2):
    return(num1 * num2)

def divided(num1, num2):
    return(num1 // num2)

def findMaxValue(arr):
    max = arr[0]
    for x in arr:
        if(max < x):
            max = x
    return max

def findMinValue(arr):
    min = arr[0]
    for x in arr:
        if(min < x):
            min = x
    return min
