def get():
    #enter 2 digits seperated by space: 
    user_x, user_y = input("Enter two values separated by space: ").split(' ')

    if user_x or user_y != int():
            #keep asking for input if the input is not digits
            while True:
                print('Enter only numbers');
                user_x, user_y = input("Enter two values separated by space: ").split(' ');
    
        #and if the user enters the word "quit" then the program must stop
        #the quit shouldn't be case sensetive
    elif user_x or user_y == (str("quit")).casefold():
        print('stuff')


    print(user_x, user_y)
    return user_x, user_y

def add(x, y):
    return x+y
   
def subtract(x, y):
    return x-y 

def division(x, y):
    return x/y

def multiply(x, y):
    return x*y


#create a "display results function"
def display_results():
    return 

results = get()

print("Addition: ", add(results[0], results[1]))
print("Subtract: ", subtract(results[0], results[1]))
print("Division: ", division(results[0], results[1]))
print("Multiply: ", multiply(results[0], results[1]))
