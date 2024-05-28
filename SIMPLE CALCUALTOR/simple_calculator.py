a=eval(input("Enter First Value "))
b=eval(input("Enter Second Value "))
operatrion = input("Enter +,-,*,/ ")
if operatrion == '+':
    print(a+b)
elif operatrion == '-':
    print(a-b)
elif operatrion == '*':
    print(a*b)
elif operatrion == '/':
    print(a/b)
else:
    print("Wrong operation")