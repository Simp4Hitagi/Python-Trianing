def add(x, y):
    return x+y 

def subtract(x, y):
    return x-y  

def multiply(x, y): 
    return x*y
 
def division(x, y):
    return x/y

def user_input():
    number1 = int(input("Give me a number : "))
    number2 = int(input("Give me another number : "))
    return number1, number2

user_info = user_input()
# 2 4

print(add(user_info[0], user_info[1]))
# print(subtract(user_input()))
# print(multiply(user_input()))
# print(division(user_input()))