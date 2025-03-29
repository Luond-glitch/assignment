def calculator():
 #Get user inputs
 number1 = float(input("Enter the first number: "))
 number2 = float(input("Enter the first number: "))
 operation = input("Enter the operation(+, -, *, /): ")

 #calculation based on te operator
 if operation == '+':
   result = number1 + number2
   print(f"{number1} {operation} {number2} = {result}")
 elif operation == '-':
   result = number1 - number2
   print(f"{number1} {operation} {number2} = {result}")
 elif operation == '*':
   result = number1 * number2
   print(f"{number1} {operation} {number2} = {result}")
 elif operation =='/':
   if number2 != 0:
       result = number1 / number2   
       print(f"{number1} {operation} {number2} = {result}")
   else:
     print("Error:Division by zero is not allowed")
 else:
   print("Invalidoperation")

# Run the calculator function
calculator()   