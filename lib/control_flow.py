#!/usr/bin/env python3


# username = "admin or ADMIN"
# password = 12345
# Write a function admin_login() that takes two arguments, a username and a password. 
#     If the username is "admin" or "ADMIN" and the password is "12345", return "Access granted".
#      Otherwise, return "Access denied".


# def admin_login(username, password):
#     # your code here
#     if username == "admin" or username == "ADMIN"  and password == 12345:
#         print("Access granted")
#     else:
#         print("Acess denied")
#     pass
# admin_login("sudo", "12345")
# admin_login("admin", "12345")
# admin_login("ADMIN", "12345")

# Write a function hows_the_weather() that takes in one argument, a temperature. 
# If the temperature is below 40, return "It's brisk out there!". 
# If the temperature is between 40 and 65, return "It's a little chilly out there!". 
# If the temperature is above 85, return "It's too dang hot out there!". Otherwise, return "It's perfect out there!"

# def hows_the_weather(temperature):
#     # your code here
#     if temperature < 40:
#         return "It's brisk out there!"
#     elif temperature >= 40 and temperature <= 65:
#         return "It's a little chilly out there!"
#     elif temperature > 85:
#         return "It's too dang hot out there!"
#     else:
#         return "It's perfect out there!"

#     pass
# print(hows_the_weather(33))
# print(hows_the_weather(99))
# print(hows_the_weather(75))
  

# Write a function fizzbuzz() takes in a number. 
# For multiples of three, return "Fizz" instead of the number. 
# For the multiples of five, return "Buzz". 
# For numbers which are multiples of both three and five, return "FizzBuzz". 
# For all other numbers, just return the number itself.

# def fizzbuzz(num):
#     # your code here
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 5 == 0:
#         print("Buzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     else:
#         print (num)

#     pass



# fizzbuzz(1)
# fizzbuzz(2)
# fizzbuzz(3)
# fizzbuzz(4)
# fizzbuzz(5)
# fizzbuzz(15)



# Write a function calculator() that takes three arguments: an operation and two numbers. 
# If the operation is one of the following: +, -, *, or /, 
# return the value of calling the operation on the two numbers. Otherwise, output a message saying "Invalid operation!" and return None.

def calculator(operation, num1, num2):
    # your code here
    if operation == '+' :
        return num1 + num2
    elif operation == '-':
        return num1 - num2 
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return None
        # print("Invalid operation!" )
    pass

print(calculator("+", 1, 1))
print(calculator("-", 3, 1))
print(calculator("*", 3, 2))
print(calculator("/", 4, 2))
print(calculator("nope", 4, 2))