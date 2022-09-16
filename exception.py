

def Sum(a,b):
    return a+b;

try: 
    a = int(input('Enter a number '))
    b = int(input('Enter a second number '))
except:
    print("Not a valid number")
else: 
    print(a+b)


