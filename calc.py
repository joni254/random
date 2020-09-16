name1 =input ("input your first name:")
print("Hello " +name1)
num1 = int(input("Enter your first number:"))
op = input("Enter your operator:")
num3 = int(input("Enter your second number:"))
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
