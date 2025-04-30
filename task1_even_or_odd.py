'''
Task 1: Even or Odd Checker
Write a function that takes a number as input and returns "Even" if it's even, or "Odd" if it's odd.
You can write it like this:

def even_or_odd(number):
    # Your code here
'''

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"



num1 = input("Enter a number: ")

try:
    anynumber = even_or_odd(int(num1)) 
    print(anynumber)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

