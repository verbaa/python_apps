x = float(input('first number: '))
y = float(input("second number"))
operation = input("operion: ")

result = None

if operation == "/":
    result = x / y
elif operation == "+":
    result = x + y
elif operation == "=":
    result = x - y
elif operation == "*":
    result = x * y
 if result is not None:
    print(result)

