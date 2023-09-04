# steps to creator a calculator.
# 1 - define the functions like add,sub,mult,div.
# 2 - input from user to choose from options.
# 3 - if choose correct go to function and run  or  please choose correct input.
# 4 - run untlie user select exit. (while True:)

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a // b

while True:
    print("Simple_Calculator")
    print("A + - Addition")
    print("S - - Subtraction")
    print("M * - Multipilcation")
    print("D / - Division")
    choice = input("input your choice: ")
    if choice.upper() == "A" or choice.upper() == "+":
        print("Addition")
        a = int(input("first input - "))
        b = int(input("second input - "))
        print(add(a,b),"\n")
    elif choice.upper() == "S" or choice.upper() == "-":
        print("Subtraction")
        a = int(input("first input - "))
        b = int(input("second input - "))
        print(sub(a,b),"\n")
    elif choice.upper() == "M" or choice.upper() == "*":
        print("Multiplication")
        a = int(input("first input - "))
        b = int(input("second input - "))
        print(mul(a,b),"\n")
    elif choice.upper() == "D" or choice.upper() == "/":
        print("Division")
        a = int(input("first input - "))
        b = int(input("second input - "))
        print(div(a,b),"\n")
    elif choice.upper() == "E" or choice.upper() == "!":
        print("Exit Program")
        exit()
    else:
        print("invalid choice\n")
