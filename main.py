def get():
    user_x = int(input('Enter x: '));
    user_y = int(input('Enter y: '));
    return user_x, user_y

def add(x, y):
    return x+y
   
def subtract(x, y):
    return x-y 

def division(x, y):
    return x/y

def multiply(x, y):
    return x*y


results = get()

print("Addition: ", add(results[0], results[1]))
print("Subtract: ", subtract(results[0], results[1]))
print("Division: ", division(results[0], results[1]))
print("Multiply: ", multiply(results[0], results[1]))




