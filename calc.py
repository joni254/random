name1 =input ("input your first name:")
print("Hello " +name1)
num1 = float(input("Enter your first number:"))
op = input("Enter your operator:")
num3 = float(input("Enter your second number:"))
if op == '*':
    print(num1 * num3)
elif op == '-':
    print(num1 - num3)
elif op == '+':
    print(num1 + num3)
elif op == '/':
    print(num1/num3)
else:
    print('invalid operator')
