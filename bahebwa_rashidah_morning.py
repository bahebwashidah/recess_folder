# Example of if, elif, and else statements in Python

# User's age
age = 25

if age < 18:
    print("You are underage.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior")
    # Example of a for loop in Python

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    # Example of a while loop in Python

count = 0

while count < 5:
    print(count)
    count += 1
    # Example of using break in a loop

fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)
    # Example of using continue in a loop

fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

for fruit in fruits:
    if fruit == "cherry":
        continue
    print(fruit)
    
    # Code that may raise an exception
try:
    # Code that might raise an exception
result = 10 / 2  # This will not raise a ZeroDivisionError
print("This line will not be executed if an exception occurs.")
except ZeroDivisionError:
    # Code to handle the specific exception
print("Oops! Division by zero is not allowed.")
except Exception as e:
    # Generic exception handler (optional)
print("An error occurred:", str(e))
finally:
    # Code that will always be executed, whether an exception occurred or not
print("This will be executed no matter what.")

# The program continues to execute after exception handling
print("Program execution continues...")
