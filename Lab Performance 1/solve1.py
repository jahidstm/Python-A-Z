# Task 1: Simple Calculator

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
    if y == 0:
       return "Error! Cannot divide by zero."
    return x / y

# --- Demonstration ---
num1 = 20
num2 = 5

print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
print(f"{num1} / {num2} = {divide(num1, num2)}")
print(f"{num1} / 0 = {divide(num1, 0)}")