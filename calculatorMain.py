print("Select an operation to select :")

print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

# I am going to take the user input below

operation = input()

if operation == "1":
    num1 = input("Enter first number :")
    num2 = input("Enter second number :")
    print("The sum is " +str(int(num1)+int(num2)))
elif operation == "2":
    num1 = input("Enter first number :")
    num2 = input("Enter second number :")
    print("The subtraction of two number is " +str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter first number :")
    num2 = input("Enter second number :")
    print("The multiplication of two number is " +str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter first number :")
    num2 = input("Enter second number :")
    print("The division of two number is " +str(int(num1) / int(num2)))
else:
    print("Invalid input :")
