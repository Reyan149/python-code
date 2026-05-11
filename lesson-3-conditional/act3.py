#Find biggest among three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2:
    if num1 > num3:
        print(f"{num1} is the biggest number.")
    else:
        print(f"{num3} is the biggest number.")
else:
    if num2 > num3:
        print(f"{num2} is the biggest number.")
    else:
        print(f"{num3} is the biggest number.") 