

# print(""" Select an option with a number \n 

# 1. Addition 
# 2. Subtraction 
# 3. Multiply 
# 4. Division 
# 5. Exponent 
# 6. Calculte Area of a square 
# 7. Square root a number
# """);

#Cast input as an int
keyboard = int(input(""" Select an option with a number \n 

1. Addition 
2. Subtraction 
3. Multiply 
4. Division 
5. Exponent 
6. Square root a number
"""))

if(keyboard == 1):
    ans1 = int(input("Enter First Number "))
    ans2 = int(input("Enter Second Number "))
    print("Answer: ", ans1 + ans2); 

if(keyboard == 2):
    ans1 = int(input("Enter First Number "))
    ans2 = int(input("Enter Second Number "))
    print('Answer: ', + ans1 - ans2); 

if(keyboard == 3):
    ans1 = int(input("Enter First Number "))
    ans2 = int(input("Enter Second Number "))
    print('Answer: ', + ans1 * ans2); 

if(keyboard == 4):
    ans1 = int(input("Enter First Number "))
    ans2 = int(input("Enter Second Number "))
    print('Answer: ' , ans1 / ans2); 

if(keyboard == 5):
    ans1 = int(input("Enter First Number "))
    ans2 = int(input("Enter Second Number "))
    print('Answer: ' , ans1 ** ans2); 

if(keyboard == 6):
    #Square root of a number
    ansN = int(input("Enter Number "))
    print("Answer: " , ansN** 0.5)

    
if(keyboard == 0):
        print("End")

