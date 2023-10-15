def add(x, y):
    return  x+y

def subtract(x, y):
    try:
        answer = x-y
    except:
        print("Answer does not match output")
    else:
        return answer
    
def division(x, y):
    try:
        answer2 = x/y
    except:
        print("Answer does not match output")
    else:
        return answer2
    

def multiply(x, y):
    return x*y   