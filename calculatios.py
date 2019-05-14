def add(num1,num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


print("Please select operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n")


ch = input("Enter your choice 1: 2: 3: 4:")


if ch == '1':
    print(num1, "+", num2, "=",
          add(num1, num2))
elif ch == '2':
    print(num1, "-", num, "=",
          subtract(num1, num2))


elif ch == '3':
    print(num1, "*", num2, "=",
          multiply(num1, num2))

elif ch == '4':
    print(num1, "/", num2, "=",
          divide(num1, numb2))
else:
    print("Invalid input")