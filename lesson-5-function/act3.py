def add (x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x//y

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
print("Enter which operation to perform, ADD, SUB, MUL, DIV")
choice = input("\n1/2/3/4")
choice = int(choice)

if choice == 1:
    print(f"The result of addition is {add(num1,num2)}")

elif choice == 2:
    print(f"The result of subtraction is {sub(num1,num2)}")

elif choice == 3:
    print(f"The result of multiplication is {mul(num1,num2)}")

elif choice == 4:
    print(f"The result of division is {div(num1,num2)}")

else:
    print("Enter a valid input.....")

